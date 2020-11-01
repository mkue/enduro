from dataclasses import dataclass
from typing import Optional

from mashumaro import DataClassMessagePackMixin


@dataclass(frozen=True)
class Metadata(DataClassMessagePackMixin):
    url: Optional[str] = None
    name: Optional[str] = None
    frame_nr: Optional[int] = None
    creation_timestamp_sec: Optional[int] = None
    sample_interval_sec: Optional[int] = None


@dataclass(frozen=True)
class Image(DataClassMessagePackMixin):
    data: bytes
    metadata: Metadata
