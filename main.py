import os

board = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

spaces = \
    [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]


def display_board(board):
    for x in range(3):
        for y in range(3):
            print(f" {board[spaces[x][y]]} ", end="")
            if y < 2:
                print("|", end="")
        if x < 2:
            print("\n-----------\n", end="")


def check_win(board):
    diag1 = board["1"] + board["5"] + board["9"]
    diag2 = board["3"] + board["5"] + board["7"]
    if diag2 == "XXX" or diag1 == "XXX":
        return "X"
    elif diag2 == "OOO" or diag2 == "OOO":
        return "O"
    for x in range(3):
        row = ""
        col = ""
        for y in range(3):
            row += board[spaces[x][y]]
            col += board[spaces[y][x]]
        if row == "XXX" or col == "XXX":
            return "X"
        elif row == "OOO" or col == "OOO":
            return "O"
    return None


win_cond = check_win(board)
cur_turn = "O"
while not win_cond:
    os.system('cls')
    print("Tic-Tac-Toe\n\n")
    display_board(board)
    if cur_turn == "X":
        cur_turn = "O"
    else:
        cur_turn = "X"
    choice_is_invalid = True
    while choice_is_invalid:
        choice = input(f"\n\nPlayer {cur_turn}, choose a remaining numbered space: ")
        if board[choice] == "X" or board[choice] == "O":
            choice_is_invalid = True
            print("That space is taken. Try again.")
        else:
            choice_is_invalid = False
    board[choice] = cur_turn
    win_cond = check_win(board)
print(f"\nPlayer {win_cond} wins!")


