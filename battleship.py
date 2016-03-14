from random import randint

board = []


for x in range(0, 5):                   #spielbrett
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)                    #zuweisen
ship_col = random_col(board)

#print ship_row             #hihi cheaterei
#print ship_col             


#Ab hier: wiederholung

for turn in range(4):
    print "Turn", turn + 1
    
    guess_row = int(raw_input("Guess Row:")) -1       #guessing
    guess_col = int(raw_input("Guess Col:")) -1      

#print ship_row             #hihi cheaterei no.2
#print ship_col

    if guess_row not in range(5) or guess_col not in range(5):  
        print "Oops, that's not even in the ocean." 

    elif (board[guess_row] [guess_col] == "X"): 
        print "You guessed that one already." 

    elif guess_row == ship_row and guess_col == ship_col:  #guess=ship
        print "Congratulations! You sank my battleship!"
        break 
    
    else: 
        print "You missed my battleship!"   #guess/=battleship
        
        board [guess_row] [guess_col] = "X"    
        print_board(board)
    
    if turn == 3: 
        print "Game Over" 
    

