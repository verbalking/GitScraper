import json
from datetime import date, datetime

import requests
from bs4 import BeautifulSoup

def calculateTime(oldtime):
    datetimeobject = datetime.strptime(oldtime,'%Y-%m-%d')
    DateCreated = datetimeobject.strftime('%Y%m%d')
    date_format = "%Y%m%d"
    DateNow = '202111'

    a = datetime.strptime(DateCreated, date_format)
    b = datetime.strptime(DateNow, date_format)
    delta = b - a
    return (delta.days) # that's it




def get_trending_repos():
    url_to_call = "https://api.github.com/search/repositories?q=created:>2020-11-30&sort=stars&order=desc"
    response = requests.get(url_to_call)

    if response.status_code != 200:
        print("Error Occurred!")

    JSONString = json.loads(response.content)
    items = JSONString['items']

    print(items[0]["name"])
    print(items[0]["description"])
    print(items[0]["stargazers_count"])
    print(items[0]["open_issues_count"])
    print(items[0]["owner"]["login"])
    print(calculateTime(items[0]["created_at"][:10]))



    <div class="container">
    <div class="card flex-row flex-wrap">
        <div class="card-header border-0">
            <img src="{{Picture}}" alt="">
        </div>
        <div class="card-block px-2">
            <h4 class="card-title">{{name}}</h4>
            <p class="card-text">{{description}}</p>
            <a href="#" class="btn btn-primary">BUTTON</a>
        </div>
        <div class="w-100"></div>

    </div>
    <br>
    <div class="card">
        <div class="row no-gutters">
            <div class="col-auto">
                <img src="//placehold.it/200" class="img-fluid" alt="">
            </div>
            <div class="col">
                <div class="card-block px-2">
                    <h4 class="card-title">Title</h4>
                    <p class="card-text">Description</p>
                    <a href="#" class="btn btn-primary">BUTTON</a>
                </div>
            </div>
        </div>

    </div>
</div>


if __name__ == "__main__":
    get_trending_repos()
