from pymongo import MongoClient
from config.config import Config

client = MongoClient(Config.MONGO_URI)
db = client['my_database']