import cv2
import numpy as np


def encode(image: np.array, encoding: str = ".png") -> bytes:
    return cv2.imencode(encoding, image)[1].tobytes()


def decode(data: bytes) -> np.array:
    return cv2.imdecode(np.asarray(bytearray(data), dtype="uint8"), cv2.IMREAD_COLOR)
