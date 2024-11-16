from pathlib import Path
import shutil
import requests
import os


def get_pic_link(api_url, payload):
    response = requests.get(api_url, params=payload)
    return response.json()["url"].lower()


def download_picture(folder, filename, url):
    file_path = os.path.join(folder, filename)
    with open(file_path, "wb") as file:
        file.write(requests.get(url).content)


def folder_refresh(folder_path):
    if Path(folder_path).exists():
        shutil.rmtree(folder_path)
    Path(folder).mkdir(parents=True, exist_ok=True)

if __name__ == '__main__':
    api_url = "https://random.dog/woof.json"
    folder = "dogs"
    folder_refresh(folder)
    for num in range(50):
        url = get_pic_link(api_url, {"filter": "mp4,webm"})
        filename = f"dog_{num + 1}{Path(url).suffix}"
        download_picture(folder, filename, url)
