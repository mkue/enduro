from dataclasses import dataclass, field
from typing import Dict, List

from envclasses import envclass


@envclass
@dataclass
class KafkaTopicConfig:
    name: str
    num_partitions: int = 1
    replication_factor: int = 1


@envclass
@dataclass
class KafkaConfig:
    boostrap_servers: List = field(default_factory=lambda: ["kafka1:19092"])
    topics: Dict[str, KafkaTopicConfig] = field(default_factory=lambda: {"image": KafkaTopicConfig("image")})


@envclass
@dataclass
class Config:
    kafka_config: KafkaConfig = KafkaConfig()
