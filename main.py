import random 
    
grid = [
        [1], [1], [1],
        [1], [], [1],
        [1], [1], [1]
    ]            

def coordToIndex(position, index = -1):
    
    if index == -1:
        pos = [*position]
        number, letter = int(pos[1]), pos[0]
        if number == 1:
            if letter == "A": return 0
            if letter == "B": return 1
            if letter == "C": return 2
        if number == 2:
            if letter == "A": return 3
            if letter == "B": return 4
            if letter == "C": return 5
        if number == 3:
            if letter == "A": return 6
            if letter == "B": return 7
            if letter == "C": return 8        
        else:
            return print("Invalid Coordinate Provided.")
        
    # Index to Position
    else:
        # Letter, Number
        row = chr(ord('A') + index // 3)
        col = str(index % 3 + 1)
        print(f'{row}{col}')

        return f'{row}{col}'
    
    
# Turn 0 -> Player 1
# Turn 1 -> Player 2           
def layout(turnSymbol, position):
    
    index = coordToIndex(position)
        
    for x in range(10):
        if x == 0:
            print("\t\tA\tB\tC")
        if x > 0 and x < 4:
            if x == 2:
                if index == 0:
                    print(f'\t1\t{turnSymbol}   |\t    |\t') 
                elif index == 1:
                    print(f'\t1\t    |\t{turnSymbol}   |\t')
                elif index == 2:
                    print(f'\t1\t    |\t    |\t{turnSymbol}')
                else:
                    print("\t1\t    |\t    |\t")
            else:   
                print("\t\t    |\t    |\t")
        if x > 3 and x < 7:
            a1format = "\t    |\t    |\t"
            if x == 5:
                if index == 3:
                    print(f'\t2\t{turnSymbol}   |\t    |\t') 
                elif index == 4:
                    print(f'\t2\t    |\t{turnSymbol}   |\t')
                elif index == 5:
                    print(f'\t2\t    |\t    |\t{turnSymbol}')
                else:
                    print("\t2\t    |\t    |\t")
            else:   
                print(f'\t{a1format}')
        if x > 6 and x < 10:
            a1format = "\t    |\t    |\t"
            if x == 8:
                if index == 6:
                    print(f'\t3\t{turnSymbol}   |\t    |\t') 
                elif index == 7:
                    print(f'\t3\t    |\t{turnSymbol}   |\t')
                elif index == 8:
                    print(f'\t3\t    |\t    |\t{turnSymbol}')
                else:
                    print("\t3\t    |\t    |\t")
            else:   
                print(f'\t{a1format}')
        if x == 3 or x == 6:
            print("\t     -----------------------")
            
        # ⭕ 🔴 🔵
        # ⛌ ❌❎ ✘

def generatedPosition(board):
    num = random.randint(0, 8)
    if len(board[num]) > 0:
        return generatedPosition(board)
    elif len(board[num]) == 0:
        return str(coordToIndex("AA", num))

while True:
    print("Hello! Are you playing solo or duo?")
    print("- \'1\' Solo")
    print("- \'2\' Duo")
    
    while True:      
        try:
            gamemode = int(input())
            if gamemode == 1 or gamemode == 2:
                break
            raise ValueError()
        except ValueError:
            print(f'Gamemode: \'{gamemode}\' is not any of the available gamemodes! Please try again.')
            continue
        
    print()
    
    # TODO: Playing duo?
    
    # Playing Solo!
    if gamemode == 1:
        print("Would you like to go first, or randomize?")
        print("- \'1\' Me First")
        print("- \'2\' Computer First")
        print("- \'3\' Randomize")
        
        
        while True:      
            try:
                choice = int(input())
                options = [1, 2, 3]
                if choice in options:
                    break
                raise ValueError()
            except ValueError:
                print(f'Choice: \'{choice}\' is not any of the available options! Please try again.')
                continue
        
        # TODO: Computer first and Randomizer
        
        #if choice == 1:
            
        
        
        break

    
    
    # TODO: Player win conditions
                
#layout("X", "C2")