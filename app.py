from fastapi import FastAPI, UploadFile, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from schemas import QuestionRequest
from background_tasks import process_document
from qa_service import answer_question

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload")
async def upload_document(file: UploadFile, bg: BackgroundTasks):
    content = await file.read()

    from ingestion import extract_text
    text = extract_text(file)

    if len(text.strip()) < 50:
        return {"message": "PDF text not readable. Try another file."}

    bg.add_task(process_document, file)
    return {"message": "Document uploaded & processing completed."}


@app.post("/ask")
def ask(req: QuestionRequest):
    answer = answer_question(req.question)
    return {"answer": answer}
