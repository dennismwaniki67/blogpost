from flask import Flask, render_template, url_for,flash
from forms import RegistrationForm,LoginForm
app = Flask(__name__)
app.config['SECRET_KEY']= '6b5818f5898dfa22b76c4222a8d5dbe4'
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

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
    return render_template('register.html',title='Register',form=form)

@app.route("/login")
def login():
    form=RegistrationForm()
    return render_template('login.html',title='Login',form=form)
    
if __name__ == '__main__':
    app.run(debug=True)