print("qwe")

class Qwe:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")

if __name__ == "__main__":
    qwe = Qwe("World")
    qwe.say_hello()