import os
import requests
import urllib.parse
from .local_settings import GOOGLE_BOOKS_KEY


# contacting the API
def lookup(text):
    try:
        # real url to api
        url = f"https://www.googleapis.com/books/v1/volumes?q={urllib.parse.quote_plus(text)}&projection=LITE&printType=books&maxResults=10&orderBy=relevance&key={GOOGLE_BOOKS_KEY}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    search = response.json()
    result = list()
    for a in search['items']:
        item = {}
        if "imageLinks" in a["volumeInfo"]:
            item["cover_url"] = a['volumeInfo']['imageLinks']['thumbnail']
        else:
            item["cover_url"] = "/static/main/default_book_cover.jpg"
        
        if "subtitle" in a["volumeInfo"]:
            item["subtitle"] = a['volumeInfo']['subtitle']
        try:
            item["id"] = a["id"]
        except KeyError as exc:
            item["id"] = None
        try:
            item["title"] = a['volumeInfo']["title"]
        except KeyError as exc:
            item["title"] = None
        try:
            item["authors"] = a['volumeInfo']['authors']
        except KeyError as exc:
            item["authors"] = None
        try:
            item["description"] = a['volumeInfo']['description']
        except KeyError as exc:
            item["description"] = None
        try:
            item["info_url"] = a['volumeInfo']['infoLink']
        except KeyError as exc:
            item["info_url"] = None
        try:
            item["categories"] = a['volumeInfo']['categories']
        except KeyError as exc:
            item["categories"] = None
        

        result.append(item)
    return result 