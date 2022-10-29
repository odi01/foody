from pymongo import MongoClient
from config import MONGO_HOST, MONGO_PORT, DATABASE
import datetime
import uuid
import structlog


log = structlog.get_logger()


class FoodyDB:
    def __init__(self):
        self.client = MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.client[DATABASE]

    def insert(self, data: dict, collection: str) -> str:
        data["uuid"] = uuid.uuid4().hex
        data["creation_date"] = datetime.datetime.utcnow()
        try:
            db_coll = self.db[collection]
            document_id = db_coll.insert_one(data).inserted_id
        except Exception as e:
            log.error("Inserted failed", collection=collection, raised_exception=str(e))
        else:
            log.info("Inserted a document", collection=collection, obj_id=document_id)
            return str(document_id)


