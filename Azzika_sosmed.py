
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Windah_Basudara"

response = requests.get(url, headers={
    "User-Agent": "Mozilla/5.0"
})

print("Status code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("h1")

if title:
    print("Judul:", title.get_text(strip=True))
else:
    print("Judul tidak ditemukan")


