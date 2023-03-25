from flask import Flask, render_template, redirect, url_for

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecret key'

class HelloForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired("Please input a name.")])
    submit = SubmitField(label="Submit")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():   # valid data entered
        print(f"{form.name.data}")
        return redirect(url_for("hello_name", name=form.name.data))
    return render_template('index.html', form=form)


@app.route('/hello')
def hello():
    return  'Hello'


@app.route('/hello/<name>')
def hello_name(name):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
