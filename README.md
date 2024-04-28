# fastapi-video-stream

Tiny project to test fastapi upload files and reproduce it.

## Installation

Install the dependencies with:

```bash
pip install -r requirements.txt
```

Execute:

```bash
uvicorn src.app:app --host localhost --port 8000 --reload
```

Now you can access the main page in http://localhost:8000/home. First upload a .mp4 file, back to home
and refresh the page to show it in main page.

Just click on video on list to navigate to another page with a player.
