from database import Base

from sqlalchemy import Column, Integer, String


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(360), unique=True)
    content = Column(String(), unique=False)
    created_at = Column(String(), unique=True)

    def __init__(self, title=None, content=None, created_at=None):
        self.title = title
        self.content = content
        self.created_at = created_at

    def __repr__(self):
        return '<article {}>'.format(self.title)
