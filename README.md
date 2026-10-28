# Lab 1: Build and Test Your First API Endpoint

In this lab you will add **one new endpoint** to an existing Python (FastAPI) backend, write **automated tests** for it, and submit a short write-up.

**What you'll do**

1. **Build** `GET /items/{item_id}`, an endpoint that returns a single item.
2. **Test** it by writing 3 tests with `pytest`.
3. **Submit** by filling in `SUBMISSION.md`, pushing to your fork, and sharing it with **`am5815`**.

Expected time: about 1–2 hours.

---

## Step 0: Fork and clone

1. Click **Fork** (top right of this page) to make your own copy of this repo under your GitHub account.
2. Clone **your fork** (replace `<your-username>`):

   ```bash
   git clone https://github.com/<your-username>/cs501_lab1.git
   cd cs501_lab1/backend
   ```

> Do all your work in your fork. You don't have permission to push to this original repo.

## Step 1: Set up the backend

You need **Python 3.10 or newer** (3.12 or 3.13 recommended). Check with `python3 --version` (or `python --version` on Windows). If yours is older, install a newer one from [python.org](https://www.python.org/downloads/).

From inside the `backend` folder, create a virtual environment and install the dependencies:

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Windows (Command Prompt)**

```bat
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

You'll know it worked when your terminal prompt starts with `(.venv)`. **Every time you open a new terminal**, `cd` into `backend` and run the `activate` line again.

### Run the API

```bash
uvicorn main:app --reload
```

Then open these in your browser:

- http://127.0.0.1:8000/test: you should see `["It's Working!"]`
- http://127.0.0.1:8000/docs: interactive docs where you can try every endpoint

Press `Ctrl+C` in the terminal to stop the server.

### Run the tests

```bash
pytest -v
```

You should see **5 passed, 3 failed**. That's expected: the 3 failing tests are the ones you will write.

## How the backend is organized

All the code is in `backend/`:

| File | What it does |
| --- | --- |
| `main.py` | The API endpoints (URLs). **You'll edit this.** |
| `crud.py` | Functions that read and write the database. **You'll edit this.** |
| `models.py` | The database tables (`User`, `Item`) |
| `schemas.py` | The shape of the JSON the API accepts and returns |
| `database.py` | Database connection (a local SQLite file, `sql_app.db`) |
| `tests/conftest.py` | Test setup: gives each test a fresh, empty database |
| `tests/test_existing.py` | Example tests for the existing endpoints. **Read these!** |
| `tests/test_items.py` | Your tests. **You'll edit this.** |

The `frontend/` folder (a React login page) is from the original lab and is **not needed** for this assignment.

## Part 1: Build the endpoint

Add a `GET /items/{item_id}` endpoint that returns one item by its id. It must behave exactly like this:

| Request | Status code | Response body |
| --- | --- | --- |
| `GET /items/1` (item 1 exists) | `200` | `{"title": "Laptop", "description": "For CS501", "id": 1, "owner_id": 1}` |
| `GET /items/9999` (no such item) | `404` | `{"detail": "Item not found"}` |
| `GET /items/abc` (not a number) | `422` | FastAPI's validation error (you get this one for free) |

**Steps**

1. **`crud.py`**: Add a function `get_item(db, item_id)` that returns the item with that id, or `None` if there isn't one. *Hint: look at `get_user`, since yours is almost the same but uses `models.Item`.*
2. **`main.py`**: Add the endpoint. *Hint: `read_user` is very close to what you need. Use `response_model=schemas.Item` and raise a 404 with `detail="Item not found"`.*
3. **Try it by hand.** With the server running, go to http://127.0.0.1:8000/docs and:
   - use **POST /users/** to create a user (note the `id` in the response),
   - use **POST /users/{user_id}/items/** to create an item for that user,
   - use **GET /items/{item_id}** to fetch it, then try an id that doesn't exist.

Your endpoint will also be checked with additional tests during grading, so match the table above **exactly** (status codes and the `detail` message).

## Part 2: Test it

Open `backend/tests/test_items.py`. It has 3 test functions, each with comments describing what to check. Replace each `pytest.fail(...)` line with real test code. `tests/test_existing.py` shows how to call the API and check responses.

Remember that every test starts with an **empty database**, so if a test needs an item, create a user and an item inside that test first.

When you're done, `pytest -v` should show **8 passed**.

> **Tip:** Make sure your tests can actually catch bugs. Temporarily break your endpoint (for example, change `"Item not found"` to something else), re-run `pytest`, and confirm a test fails. Then undo the change.

## Part 3: Write up your deliverable

Open `SUBMISSION.md` in the repo root and fill in every section:

1. Your name, BU email, and GitHub username
2. The full output of `pytest -v`
3. The JSON your endpoint returns for an existing item and for a missing one
4. Two short reflection answers

## How to submit

1. **Commit and push** your work to your fork:

   ```bash
   git add .
   git commit -m "Add GET /items/{item_id} endpoint and tests"
   git push
   ```

2. **Share your fork with me.** On GitHub, open your fork, then go to **Settings → Collaborators → Add people**, enter **`am5815`**, and send the invite.

3. **Double-check** on GitHub that your fork shows your changes to `backend/crud.py`, `backend/main.py`, `backend/tests/test_items.py`, and `SUBMISSION.md`.

The latest commit on your fork's default branch is what gets graded.

## Grading checklist

- [ ] `GET /items/{item_id}` returns `200` and the item's JSON for an existing item
- [ ] It returns `404` with `{"detail": "Item not found"}` for a missing item
- [ ] Your 3 tests in `tests/test_items.py` are real tests and they pass
- [ ] The 5 existing tests still pass
- [ ] `SUBMISSION.md` is completely filled in
- [ ] `am5815` has been added as a collaborator on your fork

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `uvicorn: command not found` or `pytest: command not found` | Your virtual environment isn't active. Run the `activate` line from Step 1 again. |
| `ModuleNotFoundError: No module named 'main'` | Run `pytest` from inside the `backend` folder. |
| `pip install` fails | Check your Python version is 3.10+ with `python3 --version`. |
| `Address already in use` when starting the server | Another server is still running. Stop it with `Ctrl+C`, or run `uvicorn main:app --reload --port 8001`. |
| Want to start over with an empty database | Stop the server and delete `sql_app.db` in the repo root. |

## Questions

Reach out to your instructor (GitHub: [@am5815](https://github.com/am5815)).

## Credits

Original lab by [Ian Saucy](https://github.com/IanSaucy/cs501_lab1).

Login page starter code: https://surajsharma.net/blog/react-login-form-typescript

FastAPI starter code: https://fastapi.tiangolo.com/tutorial/sql-database
