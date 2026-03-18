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

def player_input(player, board):
    print(f"Player {player}'s turn...")
    row = int(input("Enter row: "))
    while row < 0 or row > 2:
        print("the number is out of range. Please enter a number in a range 0-2")
        row = int(input("Enter row: "))

    column = int(input("Enter column: "))

    while column < 0 or column > 2:
        print("the number is out of range. Please enter a number in a range 0-2")
        column = int(input("Enter column: "))
    
    if board[row][column] == " ":
        board[row][column] = f"{player}"
    else:
        while board[row][column] != " ":
            print("The slot is taken. Please choose another slot:")
            row = int(input("Enter row: "))
            column = int(input("Enter column: "))

        board[row][column] = f"{player}"

def check_rows(board, player):
    #check rows
    print("check rows")
    for i in range(3):
        check = 0
        for j in range(2):
            print(f"[{i}][{j}] = {board[i][j]}")
            if board[i][j] == " ":
                break
            elif board[i][j] == board[i][j + 1]:
                check = check + 1
                print(f"[{i}][{j + 1}] = {board[i][j + 1]}, check = {check}")
        if check == 2:
            print(f"Player {player} won!")
            return 1
    return 0

def check_columns(board, player):
    #check columns
    print("check columns")
    for i in range(3):
        check = 0
        for j in range(2):
            print(f"[{j}][{i}] = {board[j][i]}")
            if board[j][i] == " ":
                break
            elif board[j][i] == board[j + 1][i]:
                check = check + 1
                print(f"[{j}][{i}] = {board[j + 1][i]}, check = {check}")
        if check == 2:
            print(f"Player {player} won!")
            return 1
    return 0

def check_diagonal_1(board, player):
    #check diagonal 1    
    print("check diagonal 1")
    check = 0    
    for j in range(2):
        print(f"[{j}][{j}] = {board[j][j]}")
        if board[j][j] == " ":
            break
        elif board[j][j] == board[j + 1][j + 1]:
            check = check + 1
            print(f"[{j}][{j}] = {board[j + 1][j + 1]}, check = {check}")
    if check == 2:
        print(f"Player {player} won!")
        return 1
    return 0

def check_diagonal_2(board, player):
    #check diagonal 2    
    print("check diagonal 2")
    check = 0    
    for j in range(2):
        print(f"[{2 - j}][{2 - j}] = {board[2 - j][2 - j]}")
        if board[2 - j][2 - j] == " ":
            break
        elif board[2 - j][2 - j] == board[1 - j][1 - j]:
            check = check + 1
            print(f"[{2 - j}][{2 - j}] = {board[1 - j][1 - j]}, check = {check}")
    if check == 2:
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

