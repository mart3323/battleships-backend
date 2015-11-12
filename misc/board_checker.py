import misc

def check(board, game):
    #check only double ships in every row
    for row in board:
        row = "".join(str(x) for x in row)
        if row.count(str(misc.SHIP)*3) > 0:
            misc.fail("3 long ships (or two ships touching horizontally) "+str(board))
        if len(row) != game.board_size:
            misc.fail("Incorrect row length")
    #check no touching in any column
    for x in range(game.board_size):
        column = "".join(str(row[x]) for row in board)
        if column.count(str(misc.SHIP)*2) > 0:
            misc.fail("Ships touching vertically")
    #check number of ships correct
    board_string = "".join("".join(str(x) for x in row) for row in board)
    if board_string.count(str(misc.SHIP)*2) != game.num_ships:
        misc.fail("Incorrect number of ships")
        return False
    return True
