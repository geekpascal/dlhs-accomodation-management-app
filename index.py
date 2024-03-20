from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='static/images')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)