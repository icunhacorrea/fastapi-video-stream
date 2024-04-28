import os

project_root_dir = os.path.dirname(__file__)

def list_videos():
    videos_path = f"{project_root_dir}/videos"
    if os.path.exists(videos_path):
        return [f for f in os.listdir(videos_path)]

