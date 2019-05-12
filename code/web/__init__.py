from io import BytesIO

import cv2
import jsonpickle
import numpy as np
import werkzeug
from flask import (Flask, Response, abort, jsonify, make_response, request,
                   send_file)
from PIL import Image

from web.errors import FaceNotFoundException
from web.operations import get_img_orientation, rotate_image

app = Flask(__name__)

ALLOWED_EXTENSIONS = ['jpg', 'jpeg']


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def main():
    return make_response('Hello world', 200)



@app.route('/fix-orientation', methods = ['POST'])
def upload_file():
    if 'file' not in request.files:
        return make_response(jsonify({'error': 'Bad Request', 'message': 'file not found'}), 400)
    file_stream=request.files['file']
    if file_stream and allowed_file(file_stream.filename):
        img=cv2.imdecode(np.fromstring(file_stream.read(),
                                         np.uint8), cv2.IMREAD_UNCHANGED)
        retval, buffer=cv2.imencode('.jpg', img)
        output=BytesIO(buffer)
        try:
            # rotate image depend on face orientation
            image=rotate_image(Image.open(output), get_img_orientation(img))
            output.seek(0)
            image.save(output, 'JPEG')
        except FaceNotFoundException as e:
            pass
        output.seek(0)
        return send_file(output,
                         as_attachment = True,
                         attachment_filename = file_stream.filename,
                         mimetype = 'image/jpeg'
                         )
    else:
        return make_response(jsonify({'error': 'Bad Request', 'message': 'file is incorrect'}), 400)
