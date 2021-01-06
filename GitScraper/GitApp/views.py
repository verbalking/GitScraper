from django.shortcuts import render
from bs4 import BeautifulSoup
import requests, json


def index(request):
    return render(request, 'GitApp/index.html')



#Function that fetches the data from the GitHub API
def FetchData(request):
    #We define the url from the github API, I added per_page=200 so we'd get enough repos
    url_to_call = "https://api.github.com/search/repositories?q=created:>2020-11-30&sort=stars&order=desc&per_page=30"

    #response is an object that contains the result of our call, we then use Json to format it
    response = requests.get(url_to_call)
    JSONString = json.loads(response.content)
    items = JSONString['items']
    items = SortData(items)

    #Item contains the structured JSON data, and we pass it on to the html file as a context dictionary
    return render(request, 'GitApp/home.html', {'items': items} )

#Function that sorts the data fetched from the github API
def SortData(json_content):
    json_content = sorted(json_content, key=lambda x : x['stargazers_count'], reverse=True)
    return json_content
