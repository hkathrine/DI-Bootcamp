def display_board(board):
    print("TIC TAC TOE")
    print("***********")
    for i in range(3):
        print("*", end=" ")

        for j in range(3):
            print(f" {board[i][j]}", end="  ")
            if j < 2:
                print("|", end=" ")
        
        print("*")
        print("* --- | --- | --- *")

def row_input(player, board):
    while 1:
        row = input("Enter row: ")
        try:
            val = int(row)
        except ValueError:
             print("Please enter a number.")
             continue    
        if (row < 0 or row > 2):
             print("the number is out of range. Please enter a number in a range 0-2")
        else:
             return row
    
def column_input(player, board):
    while 1:
        column = input("Enter column: ")
        try:
            val = int(column)
        except ValueError:
             print("Please enter a number.")
             continue    
        if (column < 0 or column > 2):
             print("the number is out of range. Please enter a number in a range 0-2")
        else:
            return column

def player_input(player, board):
    print(f"Player {player}'s turn...")
    row = row_input(player, board)
    column = column_input(player, board)

    while board[row][column] != " ":
        print("The slot is taken. Please choose another slot:")
        row = row_input(player, board)
        column = column_input(player, board)

    board[row][column] = f"{player}"

def check_rows(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            print(f"Player {player} won!")
            return 1
    return 0

def check_columns(board, player):
    #check columns
    print("check columns")
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]==player:
            print(f"Player {player} won!")
            return 1
    return 0

def check_diagonal_1(board, player):
    #check diagonal 1    
    if board[0][0] == board[1][1] == board[2][2] == player:
        print(f"Player {player} won!")
        return 1
    return 0

def check_diagonal_2(board, player):
    #check diagonal 2    
    if board[0][2] == board[1][1] == board[2][0] == player:
        print(f"Player {player} won!")
        return 1
    return 0

def check_win(board, player):
    
    if check_rows(board, player) == 1:
        return 1
    elif check_columns(board, player) == 1:
        return 1
    elif check_diagonal_1(board, player) == 1:
        return 1
    elif check_diagonal_2(board, player) == 1:
        return 1
    return 0

def check_tie(board):
    for row in board:
        for item in row:
            if item == " ":
                return 0
    print(f"it is a tie!")
    return 1

def play():
    game_board = [[" " for _ in range(3)] for _ in range(3)]
    finish = 0
    player = "X"
    i = 1
    while(finish == 0):
        if (i % 2 != 0):
            player = "X"
        else:
            player = "O"    
        display_board(game_board)
        player_input(player, game_board)
        finish = check_win(game_board, player)
        if finish == 0:
            finish = check_tie(game_board)
        i = i + 1

play()

