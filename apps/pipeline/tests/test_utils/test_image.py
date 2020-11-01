import cv2
import numpy as np

from utils.image import encode, decode


def test_encoding_decoding():
    image = cv2.imread("/tests/resources/sample.jpg")
    image_bytes = encode(image, ".png")
    image_restored = decode(image_bytes)
    assert np.array_equal(image_restored, image), "Restored image different to original one"
