import http.client, urllib.parse
import json
from .models import News
import requests
from bs4 import BeautifulSoup

# Images Api
def search_images(query, api_key, cx):
    """
    The search_images function takes in a query, api_key, and cx as parameters.
    It then uses the requests library to make a GET request to the Google Custom Search API.
    The response is parsed into JSON format using .json() and stored in response_json. 
    The image link is extracted from the JSON object and returned.
    
    :param query: Search for a specific image
    :param api_key: Authenticate the user
    :param cx: Specify the search engine to use
    :return: A link to an image
    :doc-author: Trelent
    """
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "searchType": "image",
        "key": api_key,
        "cx": cx,
        "num": 1
    }
    response = requests.get(url, params=params)
    response_json = response.json()
    image_link = response_json["items"][0]["link"]
    return image_link

# News Api

def import_data_from_api():
    """
    The import_data_from_api function is used to import data from the api.mediastack.com API,
        and store it in the database as News objects.
    
    :return: A list of dictionaries, each dictionary contains the data for one news
    :doc-author: Trelent
    """
    conn = http.client.HTTPConnection('api.mediastack.com')

    params = urllib.parse.urlencode({
        'access_key': '31333f9d4a88e9a014fea6b75757631d',
        'categories': 'technology',
        'sort': 'published_desc',
        'keywords': 'programming it ia',
        'limit': 15,
        'languages': 'en'
        })
    
    conn.request('GET', '/v1/news?{}'.format(params))
    res = conn.getresponse()
    if res.status == 200:

        News.objects.all().delete()

        print("Api responded successfully")
        data = res.read()
        data = data.decode('utf-8')
        news_json_data = json.loads(data)
        for new in news_json_data['data']:
            title = new['title']
            if not News.objects.filter(title=title).exists():
                image_link = search_images(title, "AIzaSyALDq5vomOfKRHon3WeF-ehf_v-jskNUC0", "c1c04e7c4f98d4693")
                new_model = News(title=new['title'], publication_datetime=new['published_at'].split('+')[0].replace('T', ' '), description=new['description'],complete_new_url=new['url'],country=new['country'], new_img_url = image_link)
                new_model.save()
    else:
        print("Error in request")