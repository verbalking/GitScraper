# GitScraper
Get the most starred repos in Github of the last 30 days

## Description
This project interacts with the GitHub API and receives a JSON file containing multiple repos, and it sorts them based on how many stars
each repo has, and then it shows them one by one, each repo in its own row, with their avatar, name, description, number of stars and issues, 
and finally the number of days that have passed since the repo was created.

## Getting Started

### Dependencies

Please use the latest updated version of this repo

*Django

*Python

*BeautifulSoup4


### Installing

*pip install Django

*pip install beautifulsoup4

*pip install requests

### Executing program

After creating an environment, just change directory to GitScraper and run the following command:

```
virtualenv -p python3 name
activate name

Python manage.py runserver
```
