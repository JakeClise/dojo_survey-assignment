from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'app secret key'

@app.route('/')
def home():
    return render_template('survey.html')

@app.route('/process', methods=["POST"])
def create_user():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/show-user')

@app.route('/show-user')
def show_user():
    return render_template('user.html',
    name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])
    

if __name__ == "__main__":
    app.run(debug=True)
