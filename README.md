# AI Changes Tracker Integration Guide

This guide explains how to integrate the AI Changes Tracker into your code assistant to automate change logging.
copy AI_TRACKER_GENIE.md to same directory as GEMINI.md
copy the GEMINI.md text into your assistant context file
## 1. Integration with Your Code Assistant

To enable the tracker, you need to include its core logic in your assistant's context. Add the following line to your main context file (e.g., `GEMINI.md`):

```markdown
Refer to **AI_TRACKER_GENIE.md** for instructions on tracking and summarizing project changes.
```

This tells your assistant to use the `AI_TRACKER_GENIE.md` file as its guide for all `ai-tracker` commands.

## 2. Testing the Integration

To ensure the tracker is working correctly, you can test it on the provided `test_folder`.

1.  **Modify a Test File**:
    Make a change to `/Users/jokerssd/Documents/ai_changes_tracker/folder/qwe.py`. For example, add a new function or modify an existing one.

2.  **Stage the Change**:
    Use Git to stage the file you just modified.
    ```bash
    git add /Users/jokerssd/Documents/ai_changes_tracker/folder/qwe.py
    ```

3.  **Run the Tracker**:
    Execute the update command to process the staged changes.
    ```bash
    ai-tracker update
    ```

4.  **Verify the Output**:
    Check the `UPDATES.md` file. You should see a new entry under the current date summarizing the changes you made to `qwe.py`.

## 3. Features and Usage

The AI Changes Tracker is designed to be simple and powerful.

### Core Features

- **Git-Aware**: Automatically detects staged changes in your Git repository.
- **AI-Powered Summaries**: Uses AI to generate concise, human-readable summaries of code changes.
- **Automatic Categorization**: Sorts changes into categories like `What's New`, `Bugfix`, and `Refactor`.
- **Structured Output**: Creates a clean and organized `UPDATES.md` file.

### Usage

The primary command is `update`.

-   **Analyze staged changes**:
    ```bash
    ai-tracker update
    ```
-   **Compare against a specific commit or branch**:
    ```bash
    # Compare against a commit
    ai-tracker update --ref <commit-hash>

    # Compare against a branch
    ai-tracker update --ref <branch-name>
    ```

## 4. Future Improvements

We are continuously working to improve the AI Changes Tracker. Here are some planned enhancements:

-   **Commit Message Integration**: Use commit messages to provide additional context for more accurate summaries.
-   **Custom Categories**: Allow users to define their own change categories.
-   **Interactive Mode**: Enable users to review, edit, and approve AI-generated summaries before they are saved.
-   **Automated Commit Hooks**: Offer an option to run the tracker automatically as a `pre-commit` hook.
