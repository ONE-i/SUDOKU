// Generating random color using HSL color
$(document).ready(function () {
    $(":root").css("--main-color", function () {
        // Getting a random integer between two values, inclusive
        const randomInt = (min, max) => {
            return Math.floor(Math.random() * (max - min + 1) + min);
        };
        var h = randomInt(0, 360);
        var s = randomInt(40, 60);
        var l = randomInt(70, 90);
        return `hsl(${h},${s}%,${l}%)`;
    })
});

function onlyNumberKey(evt) {
    // Only ASCII character in that range allowed
    var ASCIICode = evt.which ? evt.which : evt.keyCode;
    if (ASCIICode > 31 && (ASCIICode < 49 || ASCIICode > 57)) return false;
    return true;
}

function newBoard() {
    $("div.message-container h3").css("display", "none");
    $.ajax({
        url: "/new_board",
        type: "GET",
        success: function (newBoard) {
            $("tbody").html(newBoard.board);
            console.log(newBoard.board);
        },
    });
}

function checkResult() {
    var boardArray = [];
    $("table#board tr").each(function () {
        var rowDataArray = [];
        var actualData = $(this).find("input");
        actualData.each(function () {
            if (parseInt($(this).val()) >= 1) {
                rowDataArray.push(parseInt($(this).val()));
            } else {
                rowDataArray.push(0);
            }
        });
        boardArray.push(rowDataArray);
    });
    $.ajax({
        url: "/check_board",
        type: "POST",
        data: JSON.stringify(boardArray),
        contentType: "application/json; charset=utf-8",
        success: function (message) {
            $("div.message-container h3").html(message);
            $("div.message-container h3").css("display", "inline");
        }
    });
}

function showResult() {
    $.ajax({
        url: "/result",
        type: "GET",
        success: function (result) {
            boardArray = result.board;
            row = 0;
            $("table#board tr").each(function () {
                col = 0;
                $(this).find("input").each(function () {
                    $(this).val(boardArray[row][col]);
                    col += 1;
                });
                row += 1;
            });
        },
    });
    // Display message for when give up
    $("div.message-container h3").html("Give up already?");
    $("div.message-container h3").css("display", "inline");
}
