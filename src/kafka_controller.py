from kafka import KafkaProducer, KafkaConsumer
import json

from config import KAFKA_BROKER, USERS_DB_COLL


def kafka_consumer_controller(topic: str):
    consumer = KafkaConsumer(topic, bootstrap_servers=KAFKA_BROKER, auto_offset_reset='earliest', group_id=None)
    return consumer
#
#
# def kafka_producer_controller(topic: str, data: dict):
#     producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)
#     producer.send(topic, json.dumps(data).encode("utf-8"))


def kafka_create_new_user(req_topic, res_topic, user_data: dict, db_obj):
    consumer = kafka_consumer_controller(req_topic)

    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)
    producer.send(req_topic, json.dumps(user_data).encode("utf-8"))

    for message in consumer:
        message = json.loads(message.value.decode())
        res = db_obj.insert(data=message, collection=USERS_DB_COLL)
        producer.send(res_topic, json.dumps(res).encode("utf-8"))



