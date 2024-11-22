import logging
import sys
import time
from threading import Thread

from kafka import KafkaConsumer, TopicPartition


def read_from_topic(kafka_consumer):
    for msg in kafka_consumer:
        if msg.key:
            print(msg.key.decode("utf-8"), " ", msg.value.decode("utf-8"))
        else:
            print(msg.value.decode("utf-8"))


def read_from_topic_with_partition(kafka_consumer, topic):
    kafka_consumer.assign([TopicPartition(topic, 1)])
    for msg in kafka_consumer:
        print(msg)


def read_from_topic_with_partition_offset(kafka_consumer, topic):
    partition = TopicPartition(topic, 0)
    kafka_consumer.assign([partition])
    last_offset = kafka_consumer.end_offsets([partition])[partition]
    for msg in kafka_consumer:
        if msg.offset == last_offset - 1:
            break


# if you want to learn about threading in python, check the following article
# https://realpython.com/intro-to-python-threading/

def configure_logger():
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)


class KafkaMessageConsumer(Thread):

    def __init__(self, topic):
        Thread.__init__(self)
        self.consumer = KafkaConsumer(bootstrap_servers='VMIP:9092',  # use your VM's external IP Here!
                                      auto_offset_reset='earliest',
                                      consumer_timeout_ms=10000)

        self.consumer.subscribe(topics=[topic])

    def run(self):
        while True:
            try:
                read_from_topic(self.consumer)
                time.sleep(30)
            except Exception as err:
                logging.info(f"Unexpected {err=}, {type(err)=}")
                time.sleep(30)


if __name__ == '__main__':
    configure_logger()
    c1 = KafkaMessageConsumer('avg_score')
    c1.start()
    c1.join()