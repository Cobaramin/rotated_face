import os

import cv2
import numpy as np
from PIL import Image

TESTING_FILENAME = os.path.join(os.path.dirname(__file__), 'take-home-yoyo1.jpg')


def test_face_orientations():
    from web.operations import face_orientations
    assert face_orientations == {
        'up': 1,
        'bottom': 3,
        'left': 6,
        'right': 8
    }


def test_get_img_orientation():
    from web.operations import get_img_orientation
    img = cv2.imread(TESTING_FILENAME)
    assert get_img_orientation(img) == 6


def test_get_rotate_image():

    def _compare_pixel(img1, img2):
        rows, cols = img1.size
        for row in range(rows):
            for col in range(cols):
                if img1.getpixel((row, col)) != img2.getpixel((row, col)):
                    return False
        return True

    from web.operations import rotate_image
    output_image = rotate_image(Image.open(TESTING_FILENAME), 6)
    test_output_image = output_image.copy()
    test_output_image.rotate(90, expand=True)

    assert output_image.size == test_output_image.size
    assert _compare_pixel(output_image, test_output_image) == True
