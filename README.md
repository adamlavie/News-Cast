# Description
News-Cast is a simple flask application for adding/deleting/listing/getting 
news articles from a remote sqlite DB using sqlalchemy.

# Deployment
## Using Docker
Run `docker run -d -p 8080:8080 adamlavie/news-cast:latest`
## Locally Using Python
* Create a virtualenv
* Run `git clone https://github.com/adamlavie/News-Cast.git`
* install the news-cast package by running `pip install /path/to/news-cast`
* Run `python /path/to/news-cast/rest_service/resources.py` 

# Usage:
### GET all articles:
`curl -X "GET" http://localhost:8080/articles`
### GET an article by it's title:
`curl -X "GET" http://localhost:8080/article/<article_title>`
### PUT a new article:
`curl -X "PUT" -d title='some_title' -d content='some content' http://localhost:8080/article/some_title`
### DELETE an existing article:
`curl -X "DELETE" http://localhost:8080/article/<article_title>`
### POST an update to an existing article:
`curl -X "POST" -d title='new_title' -d content='new content' http://localhost:8080/article/<article_title>`

# Tests
* Install the test-requirements by running `pip install -r test-requirements.txt` inside your virtualenv.
* Run `nosetests tests/test_article_api.py`
