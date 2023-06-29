from fastapi import FastAPI, File, UploadFile
from preprocessing import output_image_file
from summarization import summarization, str_summarization
import shutil
import pytesseract

app = FastAPI()


@app.post("/ocr")
def ocr(image: UploadFile = File(...)):
    filePath = "imageFile"
    ocr_filepath = "ocrText"
    with open(filePath, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    filePath = output_image_file(filePath)

    ocr_txt = pytesseract.image_to_string(
        filePath, lang="eng", output_type=pytesseract.Output.STRING
    )

    with open(ocr_filepath, "w+") as buffer:
        buffer.write(ocr_txt)

    return ocr_txt


@app.post("/summary")
def summary(text: UploadFile = File(...)):
    filePath = "txtFile"

    with open(filePath, "w+b") as buffer:
        shutil.copyfileobj(text.file, buffer)

    return summarization(filePath)


@app.post("/ocr_summary")
def ocr_summary(image: UploadFile = File(...)):
    filePath = "imageFile"

    with open(filePath, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    filePath = output_image_file(filePath)

    ocr_txt = pytesseract.image_to_string(
        filePath, lang="eng", output_type=pytesseract.Output.STRING
    )

    return {
        "Summary of OCR Text": str_summarization(ocr_txt),
        "Origin OCR Text": ocr_txt,
    }
