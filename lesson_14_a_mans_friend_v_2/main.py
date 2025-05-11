import os
import requests
import shutil
from pathlib import Path


def download_picture(folder, filename, picture_link):
    file_path = os.path.join(folder, filename)
    picture_obj = requests.get(picture_link)
    with open(file_path, "wb") as file:
        file.write(picture_obj.content)


if __name__ == "__main__":
    folder = "dogs"
    payload = {"filter": "mp4,webm"}
    url = "https://random.dog/woof.json"

    if Path(folder).exists():
        shutil.rmtree(folder)
    Path(folder).mkdir(parents=True, exist_ok=True)

    for num in range(50):
        response = requests.get(url, params=payload)
        picture_link = response.json()["url"]
        picture_extension = Path(picture_link).suffix
        filename = f"dog_{num}{picture_extension.lower()}"
        download_picture(folder, filename, picture_link)
