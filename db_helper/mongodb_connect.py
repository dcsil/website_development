import datetime
import json
import os
from bson import ObjectId
from dotenv import load_dotenv
from typing import List, Optional, TypedDict
import certifi

from pymongo import MongoClient
from pymongo.collection import Collection

load_dotenv()

DB_STR = os.environ.get("DB_STR")


class ACountStats(TypedDict):
    followerCount: int
    followingCount: int
    heart: int
    heartCount: int
    videoCount: int
    diggCount: int


class AuthorStats(TypedDict):
    id: str
    nickname: str
    avatar: str
    signature: str
    region: str
    stats: ACountStats


class VCountStats(TypedDict):
    diggCount: int
    shareCount: int
    commentCount: int
    playCount: int


class VideoStats(TypedDict):
    id: str
    description: str
    epoch_create_time: int
    create_location: str
    stats: VCountStats
    label_list: List[str]


class InfluencerInfo(TypedDict):
    url: str
    author_stats: AuthorStats
    video_list: VideoStats


class UserInfo(TypedDict):
    name: str
    password: str
    likes: List[dict]
    history: List[dict]


client: MongoClient = MongoClient(DB_STR, tlsCAFile=certifi.where())

DB = client.Influencer_Web
# INFLU_COL = DB.influencer_info
# USER_COL = DB.user_info

influ_col: Collection[InfluencerInfo] = client.Influencer_Web.influencer_info
user_col: Collection[UserInfo] = client.Influencer_Web.user_info


# influencer collection query
def get_one_influencer(author_id: str):
    query = influ_col.find_one({"author_stats.id": author_id})
    return query


def get_all_influencer():
    query = influ_col.find()
    return list(query)


# user collection query
def get_one_user(username: str):
    query = user_col.find_one({"username": username})
    return query


def insert_one_user(user_info: dict):
    query = user_col.insert_one(user_info)
    return "Success"


def update_one_user(user_info):
    username = user_info["username"]

    query = get_one_user(username)
    if query:
        # replace

        user_col.replace_one({"username": username}, user_info)
    else:
        user_col.insert_one(user_info)
    return "Success"


def update_user_history(username: str, influ_id: Optional[str], mode: str):
    user_info = get_one_user(username)
    time = datetime.datetime.now().timestamp()
    if not user_info:
        return "User not exist"

    if mode == "delete":
        user_info['history'] = []
    else:
        update = False
        for i, history in enumerate(user_info['history']):
            if history['influ_id'] == influ_id:
                # update history by time
                if mode == "post":
                    history['time'] = time
                    update = True
                    break
        if not update:
            user_info['history'].append({
                "influ_id": influ_id,
                "time": time
            })

    update_one_user(user_info)
    return user_info


def update_user_likes(username: str, influ_id: str, mode: str):
    user_info = get_one_user(username)
    time = datetime.datetime.now().timestamp()
    if not user_info:
        return "User not exist"

    for i, like_info in enumerate(user_info['likes']):
        if like_info['influ_id'] == influ_id:
            if mode == "post":
                return "Like already exist"
            elif mode == "delete":
                user_info['likes'].pop(i)
                update_one_user(user_info)
                return user_info

    if mode == 'post':
        like_info = {
            'influ_id': influ_id,
            'time': time
        }
        user_info['likes'].append(like_info)
        update_one_user(user_info)

    return user_info


def update_username(username: str, new_name):
    user_info = get_one_user(username)
    user_info['username'] = new_name
    user_col.replace_one({"username": username}, user_info)
    return user_info


def update_password(username: str, password):
    user_info = get_one_user(username)
    user_info['password'] = password
    user_col.replace_one({"username": username}, user_info)
    return user_info


if __name__ == '__main__':
    print(DB.list_collection_names())
    #
    # SAMPLE_USER = {
    #     "username": "user1",
    #     "password": "pass1",
    #     "likes": [],
    #     "history": []
    # }
    # insert_one_user(SAMPLE_USER)
