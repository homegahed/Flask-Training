from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/you-url', methods = ['GET', 'POST'])
def you_url():

    if request.method == 'POST':
        return render_template('you_url.html', code=request.form['code'])
    else:
        return 'This is not valid'
