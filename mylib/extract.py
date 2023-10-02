import requests

def extract(
    url="https://raw.githubusercontent.com//workspaces/Jiechen_Li_Mini_5_SQLite/mylib/spotify_2023_1.csv", 
    file_path="spotify_2023_1.csv"
):
    """Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path