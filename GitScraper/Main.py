import requests
from bs4 import BeautifulSoup

def get_trending_repos():
    url_to_call = "https://github.com/trending"
    response = requests.get(url_to_call)
    if response.status_code != 200:
        print("Error Occurred!")
    html_content = response.content
    dom = BeautifulSoup(html_content, 'html.parser')
    all = dom.select("article.Box-row h1")
    for each_repo in all:
        href_link = each_repo.a.attrs["href"]
        name = href_link[1:]
        print(href_link)
        print(name)



if __name__ == "__main__":
    get_trending_repos()
