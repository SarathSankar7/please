from flask import Flask, render_template
import os
app = Flask(__name__)
app.config['SECRET-KEY'] =os.environ.get('SECRET_KEY','XYZ')
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about/')
def about():
    return render_template('about.html')
@app.route('/services/')
def serv():
    return render_template('serv.html')
if __name__ == '__main__':
    app.run(debug=True)