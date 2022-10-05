from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('./index.html')


# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)