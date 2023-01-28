from flask import Flask, render_template, Response, redirect, request
from werkzeug.utils import secure_filename
import os, json, tempfile

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/catch", methods=["POST"])
def catch():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect("/") #tmp
        file = request.files["file"]
        if file and allowed_file(file.filename):
            tFile = tempfile.TemporaryFile()
            tFile.write(file.read())
            tFile.seek(0)
            # call jadens beautiful function and get json response
            return page(tFile)
        else:
            return redirect("/") # tmp
    else:
        return Response("{'msg':'Error: POST method required.'}", status=200)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() == "py"

def page(lines):
    lines.seek(0)
    data = json.loads("""{"functionA":{"sorted_list":{"name":"sorted_list","type":"list","operations":[[["append",[1]],["__delitem__",[0]]]]}}}""")
    return render_template("file.html", txt=lines.read().decode("utf-8"), actions=data)
app.run(debug=True)