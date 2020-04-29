from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Borey Schafer',
        'title': 'Pitch Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'JOHN Doe',
        'title': 'Pitch Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)