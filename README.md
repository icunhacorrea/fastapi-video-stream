# fastapi-video-stream

Tiny project to test fastapi upload files and reproduce it.

## Installation

Install the dependencies with:

```bash
pip install -r requirements.txt
```

Then, execute:

```bash
uvicorn src.app:app --host localhost --port 8000 --reload
```

Now you can access the main page at http://localhost:8000/home. First, upload a .mp4 file, return to the home page, and refresh it to display the file on the main page.

Simply click on the video in the list to navigate to another page with a player.
