import requests
import time
from typing import List, Tuple
import config


def get(url, params={}, timeout=5, max_retries=5, backoff_factor=0.3):
    """ Выполнить GET-запрос

    :param url: адрес, на который необходимо выполнить запрос
    :param params: параметры запроса
    :param timeout: максимальное время ожидания ответа от сервера
    :param max_retries: максимальное число повторных запросов
    :param backoff_factor: коэффициент экспоненциального нарастания задержки
    """
    for i in range(max_retries):
        try:
            res = requests.get(url, params=params, timeout=timeout)
            return res
        except requests.exceptions.RequestException:
            if i == max_retries - 1:
                raise
            backoff_value = backoff_factor * (2 ** i)
            time.sleep(backoff_value)


def get_friends(user_id, fields):
    """ Вернуть данных о друзьях пользователя

    :param user_id: идентификатор пользователя, список друзей которого нужно получить
    :param fields: список полей, которые нужно получить для каждого пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"
    domain = "https://api.vk.com/method"
    access_token ="571de3cdaf51dfcc65d1fec21afc220119141f26960b40a457b3aa389cff2722fbbb4cdfb4e2145b012ab"
    fields = "bdate"
    v = '5.103'

    query = f"{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v={v}"
    response = get(query)
    print(response.json())
    c=int(response.json()['response']['count']) # Нвшли число записей о  друзьях
    friend_list=[]
    for i in range(0,c):
        friend_list.append(0)
    for i in range(0,c):
        friend_list[i]=response.json()['response']['items'][i]
        friend_list[i]=friend_list[i].get(fields)
    return friend_list
get_friends(127923722,'bdate')