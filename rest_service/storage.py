import datetime

from models import Article
from database import db_session
from rest_exceptions import ArticleNotFound, ArticleAlreadyExists

from flask import current_app


class StorageClient(object):

    def get_articles(self):
        return Article.query.all()

    def create_article(self, title, content):
        article = Article.query.filter_by(title=title).first()
        if article:
            raise ArticleAlreadyExists('Article with title {} already exists'
                                       .format(title))
        created_at = str(datetime.datetime.now())
        article = Article(title=title, content=content, created_at=created_at)
        db_session.add(article)
        db_session.commit()
        return article

    def get_article(self, title):
        article = Article.query.filter_by(title=title).first()
        if not article:
            raise ArticleNotFound('Article with title {} not found.'
                                  .format(title))
        return Article.query.filter_by(title=title).first()

    def update_article(self, title, new_title=None, content=None):
        article = self.get_article(title=title)
        if not article:
            raise ArticleNotFound('Article with title {} not found'
                                  .format(title))

        if new_title:
            article.title = new_title
        if content:
            article.content = content
        db_session.commit()
        return self.get_article(title=article.title)

    def delete_article(self, title):
        article = Article.query.filter_by(title=title)
        if not article:
            raise ArticleNotFound('Article with title {} doesn\'t exist'
                                  .format(title))
        result = article.first()
        article.delete()
        db_session.commit()
        return result


def get_storage_client():
    """Get the current Flask app's storage client, create if necessary
    """
    storage_client = current_app.config.get('storage_client')
    if not storage_client:
        current_app.config['storage_client'] = StorageClient()
        storage_client = current_app.config.get('storage_client')
    return storage_client
