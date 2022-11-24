import json
import os
from bson import ObjectId
from dotenv import load_dotenv
from typing import List, TypedDict
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
    likes: List[str]
    history: List[str]


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
    return query


# user collection query
def get_one_user(username: str):
    query = user_col.find_one({"name": username})
    return query


def insert_one_user(user_info: dict):
    query = user_col.insert_one(user_info)
    return "Success"


def update_one_user(user_info):
    # check if already store in DB
    username = user_info["name"]

    query = get_one_user(username)
    # exists, update
    if query:
        pass
    # insert
    user_col.replace_one({"name": username}, user_info)
    return "Success"


if __name__ == '__main__':
    print(DB.list_collection_names())
    #
    # SAMPLE_USER = {
    #     "name": "user1",
    #     "password": "pass1",
    #     "likes": [],
    #     "history": []
    # }
    # insert_one_user(SAMPLE_USER)
