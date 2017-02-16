import json

import responses

from flask import Flask, request
from database import init_db
from flask_restful import marshal_with, Resource, Api


from storage import get_storage_client

app = Flask(__name__)

api = Api(app=app)


class Articles(Resource):
    @marshal_with(responses.Article.resource_fields)
    def get(self):
        return get_storage_client().get_articles(), 200


class Article(Resource):
    @marshal_with(responses.Article.resource_fields)
    def get(self, title=None):
        return get_storage_client().get_article(title=title)

    @marshal_with(responses.Article.resource_fields)
    def delete(self, title=None):
        return get_storage_client().delete_article(title=title), 202

    @marshal_with(responses.Article.resource_fields)
    def put(self, title=None):
        form = request.form
        content = form.get('content')
        return get_storage_client().create_article(title=title,
                                                   content=content), 201

    @marshal_with(responses.Article.resource_fields)
    def post(self, title=None):
        data = request.form
        content = data.get('content')
        new_title = data.get('title')
        return get_storage_client().update_article(title,
                                                   new_title=new_title,
                                                   content=content), 200


api.add_resource(Article, '/article/<title>', endpoint='article/<title>')
api.add_resource(Articles, '/articles', endpoint='articles')


def handle_invalid_usage(error):
    response = error.__dict__
    return json.dumps(response), response.get('status_code', 500)


api.handle_error = handle_invalid_usage

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080)
