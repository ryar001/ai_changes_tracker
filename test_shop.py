import shopify
from datetime import datetime
from typing import List, Dict, Any, Optional


class ShopifyApi:
    """
    A pure-method style Shopify API wrapper for pulling sales data.
    The `shopify_api` engine instance must be passed in — 
    this class does not manage API authentication or sessions.
    """

    def __init__(self, shopify_api: shopify, session: Optional[shopify.Session] = None):
        """
        Args:
            shopify_api: The imported shopify module or API engine.
            session: An optional pre-authenticated Shopify session object.
        """
        self.shopify_api = shopify_api
        self.session = session

    def get_orders(
        self,
        status: str = "any",
        created_at_min: Optional[datetime] = None,
        created_at_max: Optional[datetime] = None,
        limit: int = 50,
    ) -> List[Dict[str, Any]]:
        """
        Fetches orders from Shopify with optional date filters.

        Args:
            status: Filter by order status ('open', 'closed', 'cancelled', 'any').
            created_at_min: Minimum creation date.
            created_at_max: Maximum creation date.
            limit: Max number of orders per page (Shopify API limit is 250).

        Returns:
            A list of order dictionaries.
        """
        params = {
            "status": status,
            "limit": limit
        }
        if created_at_min:
            params["created_at_min"] = created_at_min.strftime("%Y-%m-%dT%H:%M:%S%z")
        if created_at_max:
            params["created_at_max"] = created_at_max.strftime("%Y-%m-%dT%H:%M:%S%z")

        orders = self.shopify_api.Order.find(**params)
        return [order.to_dict() for order in orders]

    def get_sales_summary(
        self,
        created_at_min: Optional[datetime] = None,
        created_at_max: Optional[datetime] = None
    ) -> Dict[str, Any]:
        """
        Summarizes total sales in a date range.

        Args:
            created_at_min: Minimum creation date.
            created_at_max: Maximum creation date.

        Returns:
            A dictionary with total_sales and total_orders.
        """
        orders = self.get_orders(
            created_at_min=created_at_min,
            created_at_max=created_at_max,
            status="any",
            limit=250
        )

        total_sales = sum(float(o.get("total_price", 0)) for o in orders)
        total_orders = len(orders)

        return {
            "total_sales": total_sales,
            "total_orders": total_orders
        }