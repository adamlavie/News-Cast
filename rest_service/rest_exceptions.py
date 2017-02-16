from flask_restful import HTTPException


class ArticleError(HTTPException):

    def __init__(self, message, status_code=None, payload=None):
        HTTPException.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload


class ArticleNotFound(ArticleError):

    def __init__(self, message, status_code=404, payload=None):
        ArticleError.__init__(self, message, status_code, payload)


class ArticleAlreadyExists(ArticleError):
    def __init__(self, message, status_code=409, payload=None):
        ArticleError.__init__(self, message, status_code, payload)
