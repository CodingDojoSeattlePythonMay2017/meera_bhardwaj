from flask import Flask, render_template, request, redirect, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "muahahah"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show')
def show():
    return render_template('show.html', first_name=request.form['first_name'])


@app.route('/valildate', methods=["POST"])
def valildate():
    if len(request.form['email']) < 1 or len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['password']) < 1 or len(request.form['confirm_password']) < 1:
        flash("You have to fill out all the things, dude")
        return redirect('/')
    elif len(request.form['password']) < 8:
        flash("Your password must be more than 8 characters!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("not a valid email address")
        return redirect('/')
    elif request.form['password'] != request.form['confirm_password']:
        flash("Your passwords must match!")
        return redirect('/')
    else:
        flash("WOOOO")
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
