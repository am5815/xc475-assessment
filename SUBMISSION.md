# Lab 1 Submission

Fill in every section below, then commit and push this file along with your code.

## About you

- **Name:**
- **BU email:**
- **GitHub username:**

## 1. Test results

From the `backend` folder, run `pytest -v` and paste the **full** output between the lines below.
All 8 tests should pass.

```text
PASTE YOUR PYTEST OUTPUT HERE
```

## 2. Your endpoint in action

Start the server (`uvicorn main:app --reload`) and use http://127.0.0.1:8000/docs to create a user
and an item for that user. Then open `http://127.0.0.1:8000/items/<your item's id>` in your browser
and paste what you see:

```json
PASTE THE RESPONSE HERE
```

Now open an item id that does **not** exist, such as `http://127.0.0.1:8000/items/9999`, and paste what you see:

```json
PASTE THE RESPONSE HERE
```

## 3. Reflection (2–4 sentences each)

**a) Your endpoint can return a 404 or a 422. What is the difference, and what causes each one?**

> Your answer here

**b) What was the trickiest part of this lab, and how did you figure it out?**

> Your answer here
