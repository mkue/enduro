import logging
from typing import Generator, Tuple

import cv2

from utils.image import encode


def video_snapshots(url: str, sample_rate_seconds: int, encoding=".png") -> Generator[Tuple[bytes, int], None, None]:
    logging.info(f"Starting reading {url}")
    video_capture = cv2.VideoCapture(url)
    success, image = video_capture.read()
    sample_interval_frame = video_capture.get(cv2.CAP_PROP_FPS) * sample_rate_seconds
    while success:
        frame_nr = video_capture.get(cv2.CAP_PROP_POS_FRAMES)
        success, image = video_capture.read()
        if frame_nr % sample_interval_frame == 0:
            yield encode(image), frame_nr
    video_capture.release()
    logging.info(f"Finished reading {url}")
