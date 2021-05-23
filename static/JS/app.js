function onlyNumberKey(evt) {
    // Only ASCII character in that range allowed
    var ASCIICode = evt.which ? evt.which : evt.keyCode;
    if (ASCIICode > 31 && (ASCIICode < 49 || ASCIICode > 57)) 
        return false;
    return true;
}

function getBoardArray() {
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
    });
}
