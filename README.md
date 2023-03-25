# Code Jam 2023 Flask Workshop
[Slides](https://docs.google.com/presentation/d/1wzmDforWp3BNHQePDN9LZ5--XBjdLfB52Ndp8a1mVAM/edit#slide=id.g516185e3d41a937c_0)


## Installation
Create app folder (flask-workshop)

Create virtual environment:
```
python -m venv venv
```

Activate virtual environment:
```bash
# Windows:
.\venv\Scripts\activate
# Linux/macOS
. venv/bin/activate
```

Install flask (installs inside virtual environment):
```
python -m pip install flask flask-wtf
```

## Intro to Flask
### Hello world

app.py:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flask!'

if __name__ == "__main__":
    app.run(debug=True)
```

### Adding more routes
```python
@app.route('/hello')
def hello():
    return  'Hello'

@app.route('/hello/<name>')
def hello_name(name):
    return  'Hello ' + name
```

### Templates
templates/index.html:
```html
<!DOCTYPE html>
<html lang="en">


<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Workshop</title>
</head>


<body>

    <!-- Add stuff here -->
   


</body>


</html>
```

In app.py
```python
from flask import Flask, render_template
...
return render_template('index.html', name=name)
```

#### **Nested templates**

templates/base.html:
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title>
</head>

<body>

    {% block content %}{% endblock %}

</body>

</html>
```

templates/index.html:
```html
{% extends 'base.html' %}

{% block title %}Homepage{% endblock %}

{% block content %}
  <p>Hello there</p>
{% endblock %}
```

Adding nav to base template:

In templates/base.html (inside body tag):
```html
<nav>
    <a href="{{ url_for('index') }}">Home</a>
    <a href="{{ url_for('hello') }}">Hello</a>
</nav>
```

### Adding styles
In base.html:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='styles/style.css') }}">
```

static/styles/styles.html:
```css
nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
}

nav li {
    float: left;
}
  
nav li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

/* Change the link color to #111 (black) on hover */
nav li a:hover {
    background-color: #111;
}
```


CSS reset (in base.html):
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/modern-css-reset/dist/reset.min.css" />
```

### User input (forms)
app.py:
```python
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
```

index.html:
```html
<form action="" method="post">
    {{ form.csrf_token }}

    {{ form.name(
    oninvalid="this.setCustomValidity('Enter a  name.')",
    oninput="this.setCustomValidity('')") }}

    {{ form.submit() }}

</form>
```

