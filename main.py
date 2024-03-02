
# Function to display the game board
def display_board(board):
    # [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    
    print("\t\tA\tB\tC")
    form = "\t\t    |\t    |\t"
    for i, row in enumerate(board):
        print(form)
        print(f'\t{i + 1}\t{row[0]}   |\t{row[1]}   |\t{row[2]}')
        print(form)
        if i < 2:
            print("\t     -----------------------")
    pass

# Function to get player's move
def get_player_move():
    while True:
        try:
            move = input("Choose a position: (Format: 1A, 2B, 3C, etc.)\n")
            
            
            
            
            moveSplit = [char for char in move]
            index, index2 = int(moveSplit[0]) - 1, int(ord(str(moveSplit[1]).upper()) - 65)
            
            if len(moveSplit) > 2 or (index > 2 or index2 > 2) or (index < 0 or index2 < 0):
                raise TypeError
            
        
            return [index, index2]
        except (IndexError, TypeError, UnboundLocalError, ValueError):
            print("Invalid input. Try again.")
            get_player_move()
    

# Function to update the game board
def update_board(board, move, player):
    board[move[0]][move[1]] = player
    pass

# Function to check if there is a winner
def check_winner(board, player):
    
    # All 3 across
    if any(all(cell == str(player) for cell in row) for row in board):
        return True
    
    # All 3 down
    if all(row[0] == str(player) for row in board):
        return True
    
    # All 3 Diagonal
    if all(board[i][i] == str(player) for i in range(3)) or all(board[i][2-i] == str(player) for i in range(3)):
        return True
        
    
    return False     

# Function to check if the board is full
def check_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True   

# Function to check if the game is a tie
def check_tie(board):
    if check_full(board) and not check_winner(board, 'X') and not check_winner(board, 'O'):
        return True
    return False

def main():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    current_player = 'X'
    
    while True:
        display_board(board)
        move = get_player_move()
        update_board(board, move, current_player)
        
        if check_winner(board, current_player):
            display_board(board)
            print(f'Player {current_player} wins!')
            break
        elif check_tie(board):
            display_board(board)
            print("It's a tie!")
            break
            
        current_player = 'O' if current_player == 'X' else 'X'
        print(f'\nPlayer\'s {current_player} turn!')
        
        
    play_again = input("Do you want to play again? (y/n)")
    if play_again.lower() == 'y':
        main()
    else: print("Thanks for playing!")
        
if __name__ == "__main__":
    main()