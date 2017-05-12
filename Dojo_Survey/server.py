from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=["POST"])
def result():

    return render_template('result.html', name=request.form["name"], location=request.form["location"], fav_lang=request.form["fav_lang"], comment=request.form["comment"])


@app.route('/back', methods=["POST"])
def back():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
