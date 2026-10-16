from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quizzes/')
def recipes():
    return render_template('quizzes.html')

@app.route('/resources/')
def about():
    return render_template('.html')

@app.route('/professional_development/')
def blog():
    return render_template('prodev.html')

# allows u to click run button
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5423, debug=True)
    