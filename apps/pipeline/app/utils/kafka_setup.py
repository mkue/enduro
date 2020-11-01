import logging

from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

from config import KafkaConfig


def create_topics(kafka_config: KafkaConfig) -> None:
    client = KafkaAdminClient(bootstrap_servers=kafka_config.boostrap_servers)
    for topic_config in kafka_config.topics.values():
        topic = NewTopic(
            topic_config.name,
            topic_config.num_partitions,
            topic_config.replication_factor,
        )
        try:
            client.create_topics([topic])
            logging.info(f"Topic {topic_config.name} created.")
        except TopicAlreadyExistsError:
            logging.info(f"Topic {topic_config.name} already existed.")
