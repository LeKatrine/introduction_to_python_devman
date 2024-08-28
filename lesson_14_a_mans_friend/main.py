import requests
import os
# from pathlib import Path

folder = "dogs"
url = "https://random.dog/woof.json"
payload = {
    "filter": "mp4,webm"
}
for num in range(10):
    response = requests.get(url, params=payload)
    link, picture_extension = os.path.splitext(response.json()["url"])
    # Второй вариант извлечения расширения
    # picture_extension = Path(response.json()["url"]).suffix
    

    filename = f"dog_{num + 1}{picture_extension.lower()}"
    print(filename)
    folder_name = "dogs"
    print(folder_name)
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    file_path = os.path.join(folder_name, filename)
    print(file_path)
    print(response.content)
    with open(file_path, "wb") as file:
        file.write(response.content)
