from flask import Flask, render_template, url_for, request, jsonify


boardTest = [
    [0, 8, 7, 0, 5, 0, 0, 3, 6],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 2, 3, 0, 0, 0, 4, 5],
    [0, 7, 3, 0, 1, 0, 0, 9, 0],
    [2, 9, 0, 5, 0, 4, 0, 7, 1],
    [0, 6, 0, 0, 8, 0, 3, 5, 0],
    [6, 2, 0, 0, 0, 3, 8, 0, 0],
    [0, 0, 9, 0, 0, 0, 0, 0, 0],
    [8, 4, 0, 0, 7, 0, 9, 2, 0]]

newBoard = [
    [1, 1, 1, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 3, 0, 0, 0, 4, 5],
    [0, 7, 3, 0, 1, 0, 0, 9, 0],
    [2, 1, 0, 1, 0, 4, 0, 7, 1],
    [0, 6, 0, 0, 1, 0, 3, 5, 0],
    [6, 2, 0, 0, 0, 3, 1, 0, 0],
    [0, 0, 9, 0, 0, 0, 0, 0, 0],
    [1, 4, 0, 0, 1, 0, 9, 1, 0]]

result = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [8, 2, 8, 8, 8, 8, 8, 2, 8],
    [8, 8, 3, 8, 8, 8, 3, 8, 8],
    [8, 8, 8, 4, 9, 4, 8, 8, 8]]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("board.html", board=boardTest)


@app.route("/check_board", methods=['POST'])
def checkBoard():
    if request.method == 'POST':
        # This is where new board array send back from client side
        # Use 'board' to check if board is complete 
        board = request.get_json()
        
        message = ''
        checkResult = True
        if checkResult == True:
            message = 'Well done'
        elif checkResult == False:
            message = 'Ehh... Try again please'
        # Test console
        for i in board:
            print(i)
        return message
    else:
        return render_template("board.html", board=boardTest)


@app.route("/new_board", methods=['GET'])
def getNewBoard():
    if request.method == 'GET':
        return jsonify(board = render_template("new_board.html", board=newBoard))
    else:
        return render_template("board.html", board=boardTest)


@app.route("/result", methods=['GET'])
def showResult():
    if request.method == 'GET':
        return jsonify(board = result)
    else:
        return render_template("board.html", board=boardTest)


if __name__ == "__main__":
    app.run(debug=True)
