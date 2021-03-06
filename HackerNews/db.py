from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scraputils import *

Base = declarative_base()
engine = create_engine("sqlite:///news.db")
session = sessionmaker(bind=engine)


class News(Base):
    __tablename__ = "news3"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    url = Column(String)
    comments = Column(Integer)
    points = Column(Integer)
    label = Column(String)

Base.metadata.create_all(bind=engine)

s = session()
news = get_news('https://news.ycombinator.com', n_pages = 10)
for i in news:
    new = News(title = i['title'],
                author = i['author'],
                url = i['link'],
               comments = i['com'],
                points = i['score'])
    s.add(new)
    s.commit()