from fastapi import FastAPI, File, UploadFile
from typing import List
import time
import pytesseract
import asyncio
import shutil
import os


def safe_file_to_server(uploaded_file, path=".", save_as="default"):
    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file_name = os.path.join(path, save_as + extension)
    with open(temp_file_name, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)

    return temp_file_name


async def read_image(image_path, lang='eng'):
    try:
        text = pytesseract.image_to_string(image_path, land=lang)
        await asyncio.sleep(2)
        return text
    except:
        return f"Error: Não foi possível processar o arquivo: {image_path}"

app = FastAPI()


@app.get("/")
def padrao():
    return {"mensagem": "use /api/v1/extract_text"}


@app.post("/api/v1/extract_text")
async def extract_text(Images: List[UploadFile] = File(...)):
    response = {}
    s = time.time()
    for image in Images:
        print("Images Uploaded: ", image.filename)
        temp_file = safe_file_to_server(image, path="./", save_as=image.filename)
        text = await read_image(temp_file)
        response[image.filename] = text
    response["Time:"] = round((time.time() - s), 2)

    return response
