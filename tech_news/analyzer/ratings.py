# Requisito 10
from pymongo import MongoClient
from decouple import config
from bson.son import SON

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news


def top_5_news():
    """Seu código deve vir aqui"""
    # somar shares_count com comments_count
    # sort by number, alfabetico
    # limite de 5
    pipeline = [
        {
            "$addFields": {
                "$totalAmount": {"$sum": ["shares_count", "comments_count"]}
            }
        },
        {"$sort": SON([("totalAmount", 1), ("title", 1)])},
        {"$limit": 5},
        {"$project": {"totalAmount": False, "_id": False}}
    ]
    result = (list(db.news.aggregate(pipeline)))
    return result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
