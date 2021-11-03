import os
import requests
import urllib.parse



# contacting the API
def lookup(text):
    try:
        # api key to the google books api service
        api_key = 'AIzaSyCZg53Tq2uabnmxrUq2iPOp_-aky7QvSb8'
        # real url to api
        url = f"https://www.googleapis.com/books/v1/volumes?q={urllib.parse.quote_plus(text)}&projection=LITE&printType=books&maxResults=10&orderBy=relevance&key={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    search = response.json()
    result = list()
    for a in search['items']:
        item = {}
        item["id"] = a["id"]
        item["title"] = a['volumeInfo']["title"]
        # 1
        if "imageLinks" in a["volumeInfo"]:
            item["img"] = a['volumeInfo']['imageLinks']['thumbnail']
        else:
            item["img"] = "/static/main/default_book_cover.jpg"
        
        if "subtitle" in a["volumeInfo"]:
            item["subtitle"] = a['volumeInfo']['subtitle']
        # 2
        # item["authors"] = a['volumeInfo']['authors'] if "authors" in a["volumeinfo"] else None
        # 3
        try:
            item["authors"] = a['volumeInfo']['authors']
        except KeyError as exc:
            item["authors"] = None
        try:
            item["description"] = a['volumeInfo']['description']
        except KeyError as exc:
            item["description"] = ''
        try:
            item["infoLink"] = a['volumeInfo']['infoLink']
        except KeyError as exc:
            item["infoLink"] = None
        try:
            item["categories"] = a['volumeInfo']['categories']
        except KeyError as exc:
            item["categories"] = ''
        

        result.append(item)
    return result 