#Make a Flask App
from flask import Flask, request, render_template

app= Flask(__name__)

@app.route('/')
def index():
    return "Method used: %s" % request.method

@app.route('/animal', methods=['GET', 'POST'])
def animal():
    if request.method == 'POST':
        return '<h2> This is the animal page</h2>'
    else:
        return '<h2> This is the animal (GET) page</h2>'

@app.route('/animal/<animalname>')
def profile(animalname):
    return render_template('Profile.html', animalname=animalname)

if __name__ == "__main__": 
    app.run(debug=True)
