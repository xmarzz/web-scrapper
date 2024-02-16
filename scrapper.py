
import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.geeksforgeeks.org/scraping-reddit-using-python/")

soup = BeautifulSoup(req.content, "html.parser")

res = soup.title

print(res.get_text())



