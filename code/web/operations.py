from PIL import Image

from face_algorithm import detect
from web.errors import FaceNotFoundException

face_orientations = {
    'up': 1,
    'bottom': 3,
    'left': 6,
    'right': 8
}

# get image orientation depend on PCN (Progressive Calibration Networks)
def get_img_orientation(img):
    height, width = img.shape[:2]
    faces = detect(img)
    if not len(faces):
        raise FaceNotFoundException('Cannot detect any face')
    face = faces[0]
    if int(face.angle) in range(-135, -45):
        return face_orientations['right']
    elif int(face.angle) in range(-45, 45):
        return face_orientations['up']
    elif int(face.angle) in range(45, 135):
        return face_orientations['left']
    else:  # bottom
        return face_orientations['bottom']

# Image rotation
def rotate_image(image: Image, code):
    temp_img = image.copy()
    if code == face_orientations['up']:
        temp_img = temp_img.rotate(180, expand=True)
    elif code == face_orientations['left']:
        temp_img = temp_img.rotate(270, expand=True)
    elif code == face_orientations['right']:
        temp_img = temp_img.rotate(90, expand=True)
    return temp_img
