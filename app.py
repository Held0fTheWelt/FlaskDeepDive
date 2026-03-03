from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__, template_folder='template')

users = {
    'Alice': {'age': 25, 'country': 'USA'},
    'Bob': {'age': 30, 'country': 'UK'},
    'Charlie': {'age': 35, 'country': 'Australia'}
}


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
        current_time=datetime.utcnow(),
        users=users
    )


@app.route('/greet/<name>')
def greet(name):
    return render_template(
        'index.html',
        title='Home',
        user=name.strip(),
        current_time=datetime.utcnow(),
        users=users
    )


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/all-users')
@app.route('/all_users')  # alternative URL (underscore)
def all_users():
    return render_template('all_users.html', users=users)


@app.route('/update-country', methods=['GET', 'POST'])
def update_country():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        country = request.form.get('country', '').strip()
        if not username or not country:
            return render_template('update_country.html', error='Name and country are required.')
        if username not in users:
            return render_template('update_country.html', error=f'User "{username}" not found.')
        users[username]['country'] = country
        return redirect(url_for('all_users'))
    return render_template('update_country.html')


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post {post_id}"


if __name__ == "__main__":
    # Launch the Flask dev server 
    app.run(host="0.0.0.0", port=5000)