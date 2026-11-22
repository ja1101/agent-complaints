from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

from models import Complaint, complaints

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request=request, name="home.html")


@app.get("/complaints")
def complaints_board(request: Request):
    return templates.TemplateResponse(
        request=request, name="complaints.html", context={"complaints": complaints}
        )


@app.post("/complaints")
def create_complaint(agent_name: str = Form(...), text: str = Form(...)):
    complaints.append(Complaint(agent_name=agent_name, text=text))
    return RedirectResponse(url="/complaints", status_code=303)


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
