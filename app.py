from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Home', user='Alice')


if __name__ == "__main__":
    # Launch the Flask dev server 
    app.run(host="0.0.0.0", port=5000)