from flask import Flask, redirect, render_template, url_for
from flask.ext.wtf import Form
from wtforms import TextField, validators

app = Flask(__name__)
app.secret_key = 'CHECK OUT THIS KEY ON GITHUB'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../app.db'

@app.route('/')
def index():
    """Homepage"""
    return "I guess this is a homepage?"

@app.route('/a-redirect')
def a_redirect():
    """Redirect"""
    return redirect(url_for('a_template'))

@app.route('/a-template')
def a_template():
    """Use a template"""
    return render_template('template.html')

class RegoForm(Form):
    """A rego form"""
    email = TextField('Email', validators=(validators.DataRequired(),
                                           validators.Email()))

@app.route('/register', methods=('GET', 'POST'))
def get_register():
    """Handle the registration form"""
    form = RegoForm()

    if form.validate_on_submit():
        return "Success"

    return render_template('template.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
