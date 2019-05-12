import cv2
from models import load_model
from utils import Window, draw_face, crop_face

from pcn import pcn_detect

if __name__ == '__main__':
    nets = load_model()
    img = cv2.imread('/home/cobaramin/Downloads/take-home-yoyo.jpg')
    # img = cv2.imread('/home/cobaramin/Downloads/mobile3.jpg')
    faces = pcn_detect(img, nets)
    for f in faces:
        print(f.x)
        print(f.y)
        print(f.width)
        print(f.angle)
        print(f.score)
        print('----')
    # ret = crop_face(img, fcaces[0])
    draw_face(img, faces[0])
    cv2.imshow("pytorch-PCN", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
