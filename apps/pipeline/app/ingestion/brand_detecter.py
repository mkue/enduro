import logging
from typing import Final

from kafka import KafkaConsumer

from config import KafkaConfig
from models import Image
from utils.image import decode


class BrandDetector:
    def __init__(self, kafka_config: KafkaConfig):
        self.consumer: Final = KafkaConsumer(
            kafka_config.topics["image"].name,
            group_id="brand_detector",
            auto_offset_reset="earliest",
            bootstrap_servers=kafka_config.boostrap_servers,
        )

    def ingest(self) -> None:
        logging.info("Start brand detection")
        for message in self.consumer:
            image_msg = Image.from_msgpack(message.value)
            image = decode(image_msg.data)
            logging.info(f"{image_msg.metadata.creation_timestamp_sec} {len(image)}")
