from flask import Flask, render_template

import os

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, './')

app = Flask(__name__, template_folder=template_path)


@app.route('/')
def hello():
    return render_template('./index.html')


app.run(host='0.0.0.0', port=5000)