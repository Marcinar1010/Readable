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

    try: 
        search = response.json()
        result = list()
        for a in search['items']:
            result.append({
                'id' : a['id'],
                'title' : a['volumeInfo']['title'],
                'authors' : a['volumeInfo']['authors']
            })
            print(result)
        return result

    except (KeyError, TypeError, ValueError):
        return None
