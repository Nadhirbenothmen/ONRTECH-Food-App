# Initialize MongoDB client
from src.dbV2.mongo_product_repository import MongoProductRepository
from src.dbV2.mongo_client_setup import get_mongo_client
from pymongo import MongoClient

DB_NAME = "carrefour"
#COLLECTION_NAME = "V2"
COLLECTION_NAME = "V3"
"""
we should have one MongoDB client and many dbs and collections
"""
# Initialize MongoDB client
mongo_client = get_mongo_client()
# Instantiate repository
carrefour_product_repository = MongoProductRepository(mongo_client = mongo_client, db_name = DB_NAME, collection_name = COLLECTION_NAME)
#print(f"default_database: {mongo_client.get_default_database()}, HOST: {mongo_client.HOST}")
