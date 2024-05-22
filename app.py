from flask import Flask
from flask import render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    print('test')
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/postdetails')
def postdetails():
    return render_template('postdetails.html')

def run():
    app.run(host='0.0.0.0', port=8000, debug=True)

if __name__ == '__main__':
    Thread(target=run).start()
