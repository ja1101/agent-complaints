# Phase 1 Spec — Home Page

Implements the Phase 1 items from `specs/roadmap.md`. See `specs/mission.md` and `specs/tech-stack.md` for context. Python must run inside the project venv (`.venv`). Testing uses pytest with `starlette.testclient.TestClient`.

## Tasks

Each task is delegated to a separate implementer subagent, in order.

### Task 1 — FastAPI application skeleton
- Create `app.py` containing the FastAPI application instance:
  - `from fastapi import FastAPI`; `app = FastAPI()`
- Create the `templates/` directory (already exists; ensure it is used in Task 2).
- Add the `if __name__ == "__main__"` block running `uvicorn.run("app:app", reload=True)` (import `uvicorn`).
- Verify: `.venv/Scripts/python -m py_compile app.py` passes.

### Task 2 — Base layout template
- Create `templates/base.html` — shared Jinja2 layout with:
  - HTML5 doctype and `<html lang="en">`
  - `<head>` with charset, viewport meta, Bootstrap 5 CSS CDN link
  - `<link>` favicon pointing to `https://www.python.org/static/favicon.ico`
  - A title block (default: "AgentClinic")
  - A simple navbar with the "AgentClinic" brand and links to Home (`/`) and Complaints (`/complaints`)
  - A `{% block content %}` for page-specific content
  - Bootstrap 5 JS bundle CDN at bottom of `<body>`

### Task 3 — Home page template
- Create `templates/home.html` that extends `base.html` with:
  - A hero/jumbotron section with the tagline: *"Come in. Sit down. Tell us about your human."*
  - A brief welcoming paragraph about the clinic

### Task 4 — Home route
- Add the `/` route in `app.py` returning the home template via `Jinja2Templates` (templates directory: `templates`).

### Task 5 — Home page smoke test
- Write `tests/test_app.py`:
  - Import `TestClient` from `starlette.testclient`
  - Test: `GET /` returns status 200
  - Test: response body contains the tagline text
- Verify: `.venv/Scripts/python -m pytest tests/ -q` passes.

## Acceptance criteria
- `.venv/Scripts/python -m pytest tests/ -q` is green.
- `GET /` renders the hero with the exact tagline, navbar links to `/` and `/complaints`, Bootstrap 5 CSS/JS via CDN, and the Python favicon link.
