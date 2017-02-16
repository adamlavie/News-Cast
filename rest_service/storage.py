import datetime

from models import Article
from database import db_session
from rest_exceptions import ArticleNotFound, ArticleAlreadyExists

from flask import current_app


class StorageClient(object):

    @staticmethod
    def get_articles():
        return Article.query.all()

    def create_article(self, title, content):
        article = Article.query.filter_by(title=title).first()
        if article:
            raise ArticleAlreadyExists('Article with title {} already exists.'
                                       .format(title))
        article = self._create_article(content, title)
        return article

    @staticmethod
    def get_article(title):
        article = Article.query.filter_by(title=title).first()
        if not article:
            raise ArticleNotFound('Article with title {} not found.'
                                  .format(title))
        return article

    def update_article(self, title, new_title=None, content=None):
        article = self.get_article(title=title)
        if not article:
            raise ArticleNotFound('Article with title {} not found.'
                                  .format(title))

        article = self._update_article(article, content, new_title)
        # Return the new, updated article
        return article

    def delete_article(self, title):
        article = Article.query.filter_by(title=title)
        if not article:
            raise ArticleNotFound('Article with title {} not found.'
                                  .format(title))
        article = self._delete_article(article)
        return article

    def _update_article(self, article, content=None, new_title=None):
        if new_title:
            article.title = new_title
        if content:
            article.content = content
        db_session.commit()
        return self.get_article(title=article.title)

    @staticmethod
    def _delete_article(article):
        result = article.first()
        article.delete()
        db_session.commit()
        return result

    @staticmethod
    def _create_article(content, title):
        created_at = str(datetime.datetime.now())
        article = Article(title=title,
                          content=content,
                          created_at=created_at)
        db_session.add(article)
        db_session.commit()
        return article


def get_storage_client():
    """Get the current Flask app's storage client, create if necessary
    """
    storage_client = current_app.config.get('storage_client')
    if not storage_client:
        current_app.config['storage_client'] = StorageClient()
        storage_client = current_app.config.get('storage_client')
    return storage_client
