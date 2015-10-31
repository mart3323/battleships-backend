def check(board, game):
    #check only double ships in every row
    for row in board:
        row = "".join(str(x) for x in row)
        if row.count("111") > 0:
            return False
        row = row.replace("11", "00")
        if row != "0"*game.board_size:
            return False
    #check no touching in any column
    for x in range(game.board_size):
        column = "".join(str(row[x]) for row in board)
        if column.count("11") > 0:
            return False
    #check number of ships correct
    board_string = "".join("".join(str(x) for x in row) for row in board)
    if board_string.count("11") != game.num_ships:
        return False

