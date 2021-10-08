from flask import Blueprint
from flask import render_template

adminbp = Blueprint("admin", __name__, static_folder="static", template_folder="template", url_prefix="/admin")


@adminbp.route("/")
def index():
    return render_template("admin_index.html")
