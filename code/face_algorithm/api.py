import cv2
import numpy as np

from face_algorithm.models import load_model
from face_algorithm.utils import crop_face, draw_face
from face_algorithm.pcn import pcn_detect


nets = load_model()

def detect(img):
    if type(img) == str:
        img = cv2.imread(img)
    winlist = pcn_detect(img, nets)
    return winlist

def crop(img, win, size=200):
    # faces = list(map(lambda win: crop_face(img, win, size), winlist))
    # return faces
    return crop_face(img, win)

def draw(img, winlist):
    list(map(lambda win: draw_face(img, win), winlist))
    return img

def show(img, is_crop=False):
    img = cv2.imread(img)
    winlist = detect(img)
    if is_crop:
        faces = crop(img, winlist)
        img = np.hstack(faces)
    else:
        draw(img, winlist)
    cv2.imshow("Show", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
