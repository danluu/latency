from flask import Flask, redirect, render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
