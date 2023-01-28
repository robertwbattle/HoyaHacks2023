from flask import Flask, render_template, Response, redirect, request
from werkzeug.utils import secure_filename
import os



UPLOAD_FOLDER = "./uploads"

ALLOWED_EXTENSIONS = {"py"}
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/catch", methods=["POST"])
def catch():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect("/") #tmp
        file = request.files["file"]
        if file.filename == "":
            return redirect("/") #tmp
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return "file saved!" #tmp
    else:
        return Response("{'msg':'Error: POST method required.'}", status=200)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app.run(debug=True)