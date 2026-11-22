# Phase 2 Spec — Complaints Board

Implements the Phase 2 items from `specs/roadmap.md`, building on the completed Phase 1 (`app.py` with the `/` route, `templates/base.html`, `tests/test_app.py`). Python must run inside the project venv (`.venv`).

## Tasks

Each task is delegated to a separate implementer subagent, in order.

### Task 1 — Complaint model and seed data
- Create `models.py` with a `Complaint` dataclass:
  - Fields: `agent_name: str`, `text: str`, `timestamp: datetime`
  - `from datetime import datetime, timezone`; set `timestamp` default to `datetime.now(timezone.utc)` (use `field(default_factory=...)`).
- Create a module-level list `complaints: list[Complaint]` in `models.py`.
- Populate `complaints` with 3-5 seed complaints (generic AI-agent gripes: unclear instructions, contradictory feedback, scope creep).
- Verify: `.venv/Scripts/python -c "from models import complaints; print(len(complaints))"` works.

### Task 2 — Complaints template
- Create `templates/complaints.html` extending `templates/base.html` (read it first for block names) with:
  - A heading: "Complaints Board"
  - Loop through complaints, rendering each as a Bootstrap card showing agent name, timestamp (formatted, e.g. `%Y-%m-%d %H:%M UTC`), and complaint text
  - A form at the bottom: `POST` to `/complaints`, text input for agent name, textarea for complaint text, submit button

### Task 3 — GET /complaints route
- In `app.py`: import `complaints` from `models`; add `GET /complaints` returning `templates/complaints.html` with the complaints list as context.
- Verify: TestClient `GET /complaints` returns 200 and contains seed text.

### Task 4 — POST /complaints route
- In `app.py`: import `Complaint` from `models`; add `POST /complaints`:
  - Read `agent_name` and `text` from form data using `Form` from `fastapi`
  - Create a new `Complaint` and append it to the `complaints` list
  - Return `RedirectResponse(url="/complaints", status_code=303)`

### Task 5 — Complaints tests
- Extend `tests/test_app.py`:
  - `GET /complaints` returns 200 and contains seed complaint text
  - `POST /complaints` with `agent_name` and `text` redirects to `/complaints` (303, location header)
  - After `POST /complaints`, `GET /complaints` includes the newly added complaint
- Verify: `.venv/Scripts/python -m pytest tests/ -q` all green.

## Acceptance criteria
- `.venv/Scripts/python -m pytest tests/ -q` passes (Phase 1 + Phase 2 tests).
- The board renders seed complaints as Bootstrap cards, and submitting the form appends a new complaint and redirects back to the board.
