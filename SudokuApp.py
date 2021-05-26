from flask import Flask, render_template, url_for, request, jsonify, redirect
from newGame import newGame


app = Flask(__name__)


@app.route("/")
def home():
    global playerBoard, resultBoard
    playerBoard, resultBoard = newGame()
    return render_template("board.html", board = playerBoard)


@app.route("/new_board", methods=['GET'])
def getNewBoard():
    if request.method == 'GET':
        global playerBoard, resultBoard
        playerBoard, resultBoard = newGame()
        return jsonify(board = render_template("new_board.html", board = playerBoard))
    else:
        return redirect('/')


@app.route("/check_board", methods=['POST'])
def checkBoard():
    if request.method == 'POST':
        # This is where new board array send back from client side
        # Use 'resultBoard' to check if 'curPlayerBoard' is complete 
        curPlayerBoard = request.get_json()
        # Test console
        for i in curPlayerBoard:
            print(i)
            
        global resultBoard
        if curPlayerBoard == resultBoard:
            return 'Well done'
        elif curPlayerBoard != resultBoard:
            return 'Ehh... Try again please'
    else:
        return redirect('/')


@app.route("/result", methods=['GET'])
def showResult():
    global resultBoard
    if request.method == 'GET':
        return jsonify(board = resultBoard)
    else:
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
