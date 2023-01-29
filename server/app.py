import flask
import flask_cors
import json
import os
import sys
import tempfile
import uuid

sys.path.append(os.pardir)

from visify.analyzer.module_macroscopic import ModuleMacroscopic

app = flask.Flask(__name__,
    static_folder=os.path.join(os.pardir, "client", "dist"),
    static_url_path="/"
)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/analyze", methods=["POST"])
@flask_cors.cross_origin()
def analyze():
    if not flask.request.files["file"]:
        return "Please provide a Python file to analyze.", 400

    with tempfile.TemporaryDirectory() as directory:
        module_name = str(uuid.uuid4())

        with open(os.path.join(directory, f"{module_name}.py"), "wb") as file:
            file.write(flask.request.files["file"].read())

        sys.path.append(directory)

        macroscopic = ModuleMacroscopic(module_name)
        macroscopic.run()

        del sys.path[-1]

    return json.dumps(macroscopic.encoded_result())
