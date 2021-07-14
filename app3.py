from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template('homepage.html', name=name)

@app.route("/loopy/<int:number>")
def loopy(number):
    return render_template("loopy.html", number=number)

if __name__=='__main__':
    app.debug=True
    app.run()