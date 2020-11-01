import logging
from dataclasses import dataclass
from functools import partial
from time import time
from typing import Final

from kafka import KafkaProducer
from config import KafkaConfig
from models import Metadata, Image
from utils.video import video_snapshots


@dataclass(frozen=True)
class VideoIngesterInput:
    url: str
    name: str
    sample_rate_seconds: int = 2


class VideoIngester:
    def __init__(self, video_ingester_input: VideoIngesterInput, kafka_config: KafkaConfig):
        self.input: Final = video_ingester_input
        self.topic: Final = kafka_config.topics["image"].name
        self.producer: Final = KafkaProducer(bootstrap_servers=kafka_config.boostrap_servers, max_request_size=3145728)
        self.metadata_partial: Final = partial(Metadata, url=video_ingester_input.url, name=video_ingester_input.name)

    def ingest(self) -> None:
        logging.info(f"Start ingesting {self.input.name}")
        for snapshot, frame_nr in video_snapshots(self.input.url, self.input.sample_rate_seconds, ".png"):
            payload = Image(
                snapshot,
                self.metadata_partial(frame_nr=frame_nr, creation_timestamp_sec=int(time())),
            )
            self.producer.send(self.topic, value=payload.to_msgpack()).add_errback(
                lambda exception: logging.error(f"Failed sending frame {frame_nr} to Kafka", exc_info=exception)
            )
        logging.info(f"Finished ingesting {self.input.name}")
