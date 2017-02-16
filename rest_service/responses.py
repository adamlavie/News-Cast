from flask_restful import fields


class Article(object):
    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.content = kwargs.get('content')
        self.created_at = kwargs.get('created_at')

    resource_fields = {
        'title': fields.String,
        'content': fields.String,
        'created_at': fields.String
    }
