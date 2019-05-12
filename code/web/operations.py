from PIL import Image

from web.errors import FaceNotFoundException

# get image orientation depend on PCN (Progressive Calibration Networks)
def get_img_orientation(img):
    height, width = img.shape[:2]
    faces = detect(img)
    if not len(faces):
        raise FaceNotFoundException('Cannot detect any face')
    face = faces[0]
    if int(face.angle) in range(-135, -45):  # right
        return 8
    elif int(face.angle) in range(-45, 45):  # up
        return 1
    elif int(face.angle) in range(45, 135):  # left
        return 6
    else:  # bottom
        return

# Image rotation
def rotate_image(image: Image, code):
    temp_img = image.copy()
    if code == 3:
        temp_img = temp_img.rotate(180, expand=True)
    elif code == 6:
        temp_img = temp_img.rotate(270, expand=True)
    elif code == 8:
        temp_img = temp_img.rotate(90, expand=True)
    return temp_img
