import pandas as pd
import requests
import textwrap
import re
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
from pandas.io.json import json_normalize
from string import Template
from tqdm import tqdm
import time

def insert_code(offset):
        return """return API.wall.get ({
        "owner_id": "",
        "domain": "itmoru",
        "offset": %s,
        "count": 0,
        "filter": "owner",
        "extended": 0,
        "fields": "text",
        "v": "5.103"
    });""" % offset

def get_wall(
    owner_id: str='',
    domain: str='',
    offset: int=0,
    count: int=10,
    filter: str='owner',
    extended: int=0,
    fields: str='',
    v: str='5.103'
):
    """
    Возвращает список записей со стены пользователя или сообщества.

    @see: https://vk.com/dev/wall.get 

    :param owner_id: Идентификатор пользователя или сообщества, со стены которого необходимо получить записи.
    :param domain: Короткий адрес пользователя или сообщества.
    :param offset: Смещение, необходимое для выборки определенного подмножества записей.
    :param count: Количество записей, которое необходимо получить (0 - все записи).
    :param filter: Определяет, какие типы записей на стене необходимо получить.
    :param extended: 1 — в ответе будут возвращены дополнительные поля profiles и groups, содержащие информацию о пользователях и сообществах.
    :param fields: Список дополнительных полей для профилей и сообществ, которые необходимо вернуть.
    :param v: Версия API.
    """


    response = requests.post(
        url="https://api.vk.com/method/execute",
            data={
                "code": insert_code(0),
                "access_token": "0cbdbb9f4047c4d8dbff47a9d79588759ae6874cd730eb44a527c6373f19e837000d9b26617f974d6599e",
                "v": "5.103"
            }
    )
    c=int(response.json()['response']['count']) # Нвшли число записей
    print(c)
    wall_posts=[]
    for i in range(1000):
        wall_posts.append(0)
    point=0
    for offset in range(0,1000,20):
        response = requests.post(
        url="https://api.vk.com/method/execute",
            data={
                "code": insert_code(offset),
                "access_token": "0cbdbb9f4047c4d8dbff47a9d79588759ae6874cd730eb44a527c6373f19e837000d9b26617f974d6599e",
                "v": "5.103"
            }
    )
        j=0
        for i in range(point, offset):
            try:
                wall_posts[i]=response.json()['response']['items'][j]
                wall_posts[i]=wall_posts[i].get('text')
                j=j+1
            except:
                print(response.json())
        point=offset
        time.sleep(0.5)
    return wall_posts



text_data=get_wall()
print(len(text_data))
print(text_data)
for i in range(0,len(text_data)):
    text_data[i]= re.sub('http\S*\/', ' ', text_data[i])
def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations
for i in range(0,len(text_data)):
    text_data[i]=list(sent_to_words(text_data))
text_data=text_data[0]
print(text_data)
for i in range(0, len(text_data)):
    for j in range(0, len(text_data[i])):
        text_data[i][j]=morph.parse(text_data[i][j])[0].normal_form
print(text_data)
