import os
import requests
import urllib.parse



# contacting the API
def lookup(text):
    try:
        # api key to the google books api service
        api_key = 'AIzaSyCZg53Tq2uabnmxrUq2iPOp_-aky7QvSb8'
        # real url to api
        url = f"https://www.googleapis.com/books/v1/volumes?q={urllib.parse.quote_plus(text)}&maxResults=10&printType=books&key={api_key}"
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
        #if "authors" in a["volumeinfo"]:
        #    item["authors"] = a['volumeInfo']['authors']
        # 2
        # item["authors"] = a['volumeInfo']['authors'] if "authors" in a["volumeinfo"] else None
        # 3
        try:
            item["authors"] = a['volumeInfo']['authors']
        except KeyError as exc:
            item["authors"] = None

        result.append(item)
    return result

    
    