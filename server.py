from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<int:num>')
@app.route('/<int:num>/<int:num1>')
@app.route('/<int:num>/<int:num1>/<color1>')
@app.route('/<int:num>/<int:num1>/<color1>/<color2>')
def playBox (num=8, num1 = 8, color1 = "black", color2 = "red"):
    return render_template("index.html", num = int(num/2), num1 = int(num1/2), color1 = color1, color2 = color2)



if __name__ == '__main__':
    app.run(debug=True, port = 5001)


