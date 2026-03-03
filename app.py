from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    name = request.args.get('name')
    if not name or not name.strip():
        name = 'Guest'
    else:
        name = name.strip()
    return render_template(
        'index.html',
        title='Home',
        user=name,
        current_time=datetime.utcnow()
    )


@app.route('/form')
def form():
    return render_template('form.html')


if __name__ == "__main__":
    # Launch the Flask dev server 
    app.run(host="0.0.0.0", port=5000)