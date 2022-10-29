from validator import is_valid_user
from config import USERS_DB_COLL, KAFKA_BROKER, KAFKA_REQUEST_TOPIC, KAFKA_RESPONSE_TOPIC

from mongo import FoodyDB


class UserController:
    def __init__(self):
        self.db_users_coll = FoodyDB()

    def user_creator(self, user_profile_data: dict) -> dict:
        if not is_valid_user(user_profile_data):
            return {"status": "error",
                    "cause": "Invalid user input"}

        insert_user = self.db_users_coll.insert(data=user_profile_data, collection=USERS_DB_COLL)
        if insert_user is None:
            return {"status": "error",
                    "cause": "database error, check the logs"}

        return {"status": "success",
                "description": "created new user",
                "document_id": str(insert_user)}
