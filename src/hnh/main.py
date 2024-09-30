from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from transformers import pipeline
from hnh.utils import get_max_label, get_max_score, get_label
from fastapi import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

html = Jinja2Templates(directory="public")

@app.get("/files/")
def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.get("/")
async def home(request: Request):
    hotdog = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxqqIG2n685k1AS3HyuhXLgMsySGTozbxNvQ&s"
    dog = "https://mblogthumb-phinf.pstatic.net/MjAyMjAyMDdfMjEy/MDAxNjQ0MTk0Mzk2MzY3.WAeeVCu2V3vqEz_98aWMOjK2RUKI_yHYbuZxrokf-0Ug.sV3LNWlROCJTkeS14PMu2UBl5zTkwK70aKX8B1w2oKQg.JPEG.41minit/1643900851960.jpg?type=w800"
    image_url = "https://cdn.pixabay.com/photo/2015/11/03/09/03/question-mark-1019983_1280.jpg"
    return html.TemplateResponse("index.html",{"request":request, "image_url": image_url})


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    # 파일 저장
    img = await file.read()
    model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")
    
    from PIL import Image
    import io
    img = Image.open(io.BytesIO(img))

    p = model(img)
    max_label = get_max_label(p)
    max_score = get_max_score(p)
    l = get_label(p)
    
    return l


