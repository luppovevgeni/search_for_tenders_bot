import pymongo
from config import DB, USER

db_client = pymongo.MongoClient(f'mongodb+srv://{USER[0]}:{USER[1]}@Cluster0.vnd3j.mongodb.net/{DB}?retryWrites=true&w=majority')

current_db = db_client[DB]

users = current_db['users']