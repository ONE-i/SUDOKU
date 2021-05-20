from flask import Flask, render_template, url_for


boardTest = [
    [0,8,7,0,5,0,0,3,6],
    [0,0,0,0,0,0,1,0,0],
    [0,0,2,3,0,0,0,4,5],
    [0,7,3,0,1,0,0,9,0],
    [2,9,0,5,0,4,0,7,1],
    [0,6,0,0,8,0,3,5,0],
    [6,2,0,0,0,3,8,0,0],
    [0,0,9,0,0,0,0,0,0],
    [8,4,0,0,7,0,9,2,0]
    ]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("board.html", board = boardTest)

if __name__ == "__main__":
    app.run(debug = True)