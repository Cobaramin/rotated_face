from io import BytesIO

import cv2
import numpy as np
from PIL import ExifTags, Image

import jsonpickle
import werkzeug
from flask import (Flask, Response, abort, jsonify, make_response, request,
                   send_file)
from pcn import detect
from web.errors import FaceNotFoundException

app = Flask(__name__)

ALLOWED_EXTENSIONS = ['jpg', 'jpeg']


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
        return 3


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

# api entry point
@app.route('/fix-orientation', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return make_response(jsonify({'error': 'Bad Request', 'message': 'file not found'}), 400)
    file_stream = request.files['file']
    if file_stream and allowed_file(file_stream.filename):
        img = cv2.imdecode(np.fromstring(file_stream.read(),
                                         np.uint8), cv2.IMREAD_UNCHANGED)
        retval, buffer = cv2.imencode('.jpg', img)
        output = BytesIO(buffer)
        try:
            # rotate image depend on face orientation
            image = rotate_image(Image.open(output), get_img_orientation(img))
            output.seek(0)
            image.save(output, 'JPEG')
        except FaceNotFoundException as e:
            pass
        output.seek(0)
        return send_file(output,
                         as_attachment=True,
                         attachment_filename=file_stream.filename,
                         mimetype='image/jpeg'
                         )
    else:
        return make_response(jsonify({'error': 'Bad Request', 'message': 'file is incorrect'}), 400)
