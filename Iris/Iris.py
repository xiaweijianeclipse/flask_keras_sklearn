from flask import Blueprint, render_template, request,redirect, url_for, flash
from joblib import load
import numpy as np
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt


irisBp = Blueprint("Iris", __name__, template_folder="template", static_folder="static", url_prefix="/Iris")


@irisBp.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("iris_index.html")
    else:
        knn_in = load("Iris/knn.joblib")
        text = request.form['text']
        np_arr = str_to_np_arr(text)
        prediction = knn_in.predict(np_arr)
        iris_dataset = load_iris()
        flash(f'预测种类为{iris_dataset["target_names"][prediction]}')
        return redirect(url_for('Iris.index'))
        #return render_template("iris_index.html", content=iris_dataset['target_names'][prediction])


def str_to_np_arr(text):
    def is_float(text):
        try:
            float(text)
            return True
        except:
            return False
    floats = np.array([float(x) for x in text.split(",") if is_float(x)])
    return floats.reshape(1, 4)
