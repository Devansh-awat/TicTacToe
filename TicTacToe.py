import random
board=[[0,0,0],
       [0,0,0],
       [0,0,0]]

def print_board():
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                print('   ',end='')
            elif board[i][j]==1:
                print(' X ',end='')
            elif board[i][j]==2:
                print(' O ',end='')
            if j!=2:
                print('│',end='')
        print()
        if i!=2:
            print('───┼───┼───')

def check_win():
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] and board[i][0]!=0:
            return board[i][0]
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=0:
            return board[0][i]
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=0:
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!=0:
        return board[0][2]
    return 0

def check_draw():
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                return False
    return True

def can_win(player):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = player
                if check_win() == player:
                    board[i][j] = 0
                    return (i, j)
                board[i][j] = 0
    return False

def two_winning_moves(player):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = player
                win_count = 0
                for x in range(3):
                    for y in range(3):
                        if board[x][y] == 0:
                            board[x][y] = player
                            if check_win() == player:
                                win_count += 1
                            board[x][y] = 0
                board[i][j] = 0
                if win_count >= 2:
                    return (i, j)
    return False

def bot_turn():
    if board==[[0,0,0],
              [0,0,0],
              [0,0,0]]:
        row=random.sample([0,2],1)[0]
        col=random.sample([0,2],1)[0]
        board[row][col]=1
    elif can_win(1) is not False:
        row, col = can_win(1)
        board[row][col] = 1
    elif can_win(2) is not False:
        row, col = can_win(2)
        board[row][col] = 1
    elif two_winning_moves(1) is not False:
        row, col = two_winning_moves(1)
        board[row][col] = 1
    else:
        while True:
            row=random.sample([0,2],1)[0]
            col=random.sample([0,2],1)[0]
            if board[row][col]==0:
                board[row][col]=1
                break
    print_board()
    if check_win()==1:
        print('You lose!')
        exit()
    if check_draw():
        print('Draw!')
        exit()
    
def player_turn():
    print('Enter the row and column number where you want to place your mark')
    row = int(input('Row: '))-1
    col = int(input('Column: '))-1
    if board[row][col]==0:
        board[row][col]=2
    else:
        print('Invalid move')
        player_turn()
    if check_win()==2:
        print('You win!')
        exit()
    if check_draw():
        print('Draw!')
        exit()

while True:
    bot_turn()
    player_turn()