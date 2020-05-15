import base64
import os
from io import BytesIO

import numpy as np
from PIL import Image
from flask import Flask, render_template, request

from common import load_model

global model
model = load_model("model")
app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict/', methods=['POST'])
def predict():
    # get data from drawing canvas and save as image
    img = request.get_data()
    img = img.split(b"base64,")[1]
    img = BytesIO(base64.b64decode(img))
    img = Image.open(img)
    img = Image.composite(img, Image.new('RGB', img.size, 'white'), img)
    img = img.convert('L')
    img = img.resize((28, 28), Image.ANTIALIAS)
    img = 1 - np.array(img, dtype=np.uint8) / 255.0
    img = img.reshape(1, 28, 28, 1)
    # reshape image data for use in neural network
    out = model.predict(img)
    response = np.array_str(np.argmax(out, axis=1))
    return response



if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
