import datetime as dt
from statistics import median
from typing import Optional

from api import get_friends



def age_predict(user_id: int) -> Optional[float]:
    """ Наивный прогноз возраста по возрасту друзей

    Возраст считается как медиана среди возраста всех друзей пользователя

    :param user_id: идентификатор пользователя
    :return: медианный возраст пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    friend_list=get_friends(user_id,"id,bdate")
    i=0
    while i<len(friend_list):
        if friend_list[i]==None or len(friend_list[i])<9 :
            del(friend_list[i])
        else:
            i=i+1
       for i in range(0,len(friend_list)):
       s=friend_list[i]
       dates_list[i]=int(s[len(s)-4:len(s)])
    return (int(2019-median(dates_list)))
print(age_predict(127923722))