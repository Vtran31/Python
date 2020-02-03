from IPython.display import clear_output

player1 = 1
player2 = 2


board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

#Begin to run game 
def RunGame() :
    p1_move = False
    count = True
    while count :
        p1_move = Player_Input(player1, player2, p1_move, board)
        Display_Board(board)
        count = Check_Winner(board)
        


# check user input
def Player_Input(player1, player2, p1_move, board):
    if p1_move == True :
        player1 = input(" PLayer1, Move (0-8): ")
        board[int(player1)] = 'X'
        p1_move = False
        print(p1_move)
    else :
        player2 = input("PLayer 2 move (0-8) :")
        board[int(player2)] = '0'
        p1_move = not p1_move
        print(p1_move)
    return p1_move
        
#display the play 
def Display_Board(board) :
    clear_output()
    
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

#check for winner 
def Check_Winner(board) :
    if  (board[0] == board[1] == board[2] != ' ') or \
        (board[3] == board[4] == board[5] != ' ') or \
        (board[6] == board[7] == board[8] != ' ') or \
        (board[0] == board[3] == board[6] != ' ') or \
        (board[1] == board[4] == board[7] != ' ') or \
        (board[2] == board[5] == board[8] != ' ') or \
        (board[0] == board[4] == board[8] != ' ') or \
        (board[2] == board[4] == board[6] != ' '):           
        print('Congraulatiom ! YOu win .')
        return False
    

    
RunGame()
    