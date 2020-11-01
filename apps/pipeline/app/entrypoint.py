import logging.config
from dataclasses import dataclass
from typing import Union

import yaml
from envclasses import load_env
from simple_parsing import ArgumentParser

from config import Config
from ingestion.brand_detecter import BrandDetector
from ingestion.video_ingester import VideoIngesterInput, VideoIngester
from utils import kafka_setup
@dataclass
class StartVideoIngester:
    input: VideoIngesterInput

    def execute(self, config: Config):
        VideoIngester(self.input, config.kafka_config).ingest()


@dataclass
class StartBrandDetector:
    def execute(self, config: Config):
        BrandDetector(config.kafka_config).ingest()


@dataclass
class Program:
    command: Union[StartVideoIngester, StartBrandDetector]

    def execute(self):
        self.configure_logging()
        config = self.create_config()
        kafka_setup.create_topics(config.kafka_config)
        return self.command.execute(config)

    @staticmethod
    def create_config() -> Config:
        config = Config()
        load_env(config)
        return config

    @staticmethod
    def configure_logging() -> None:
        with open('resources/logging.yml', "r") as stream:
            logging_config = yaml.load(stream, Loader=yaml.SafeLoader)
        logging.config.dictConfig(logging_config)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_arguments(Program, dest="program")
    program: Program = parser.parse_args().program
    program.execute()
