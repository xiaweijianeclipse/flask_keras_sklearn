import os.path

from flask import Blueprint
from flask import render_template, jsonify, request
import base64
import numpy as np
import io
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential, load_model
from keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array
from flask import request
from flask import jsonify
from flask import Flask

dogCatBlueprint = Blueprint("dogCat", __name__, template_folder="template", static_folder="static")


def get_model():
    global model
    model = load_model("./models/dog_cat_model1.h5")


get_model()


def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    return image


@dogCatBlueprint.route("/index")
def index():
    return render_template("index.html")


@dogCatBlueprint.route("/")
def home():
    return render_template("home.html")


@dogCatBlueprint.route("/dog-cat")
def train_dog_cat():
    return render_template("dog_cat.html")


@dogCatBlueprint.route("/predict", methods=["POST"])
def predict():
    json_data = request.get_json(force=True)
    encoded = json_data['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(224, 224))
    prediction = model.predict(processed_image).tolist()

    response = {
        'prediction': {
             'dog': prediction[0][1],
             'cat': prediction[0][0]
        }
    }

    return jsonify(response)



