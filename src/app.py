import aiofiles

from typing import Annotated
from pathlib import Path

from fastapi import FastAPI, Header, Request, Response, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from .utils import list_videos

templates = Jinja2Templates(
    directory="src/templates"
)
video_path = "src/videos"

origins = [
    "*"
]

app = FastAPI(
    title="FastAPI video live stream test",
    summary="Project example to show local video in browser."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", status_code=200)
async def root():
    return {"message": "FastAPI Live stream project."}

@app.get("/home", response_class=HTMLResponse, status_code=200)
async def home(request: Request):
    videos = list_videos()
    print(videos)
    return templates.TemplateResponse(
        "home.html", context={
            "request": request,
            "videos": videos
        }
    )

@app.get("/video/{url}", status_code=200)
async def video_tag(url: str, request: Request):
    print(url)
    return templates.TemplateResponse("video.html", context={
        "request": request,
        "url": url
    })

@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    out_url = f"{video_path}/{file.filename}"

    async with aiofiles.open(out_url, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)

    return {"File saved": "ok"}

@app.get("/video/reproduce/{url}")
async def reproduce_video(url: str, range: str = Header(None)):
    start, end = range.replace("bytes=", "").split("-")
    print(range, start, end)
    start = int(start)
    end = int(end) if end else start + (1024 * 1024)

    video_url = Path(f"{video_path}/{url}")
    with open(video_url, "rb") as video:
        video.seek(start)
        data = video.read(end - start)
        filesize = str(video_url.stat().st_size)

        headers = {
            'Content-Range': f'bytes {str(start)}-{str(end)}/{filesize}',
            'Accept-Ranges': 'bytes'
        }

        return Response(data, headers=headers, media_type="video/mp4")

