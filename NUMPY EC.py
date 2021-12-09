# Write a script to play two-dimensional Tic-Tac-Toe between a human player 
# and the computer. Use a 3-by-3 two-dimensional array. Each player indicates 
# their moves by entering a pair of numbers representing the row and column indices 
# of the square in which they want to place their mark, either an 'X' or an 'O'. 
# When the first player moves, place an 'X' in the specified square. With the 
# computer choice, place an 'O' in the specified square. Each move must be to an 
# empty square. After each move, determine whether the game has been won and whether 
# it’s a draw. Also, allow the player to specify whether he or she wants to go first 
# or second.

import random

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end=' ')
        print('\n', end ='')

def win_or_draw(grid):
    for row in grid:
        if row[0] == row[1] and row[0] == row[2] and row[0] != '.':
            if row[0] == '0':
                print('COMPUTER WON!')
            else:
                print('YOU WON!')
            return True

    if grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2] and grid[0][0] != '.':
        if grid[0][0] == '0':
            print('COMPUTER WON!')
        else:
            print('YOU WON!')
        return True

    if grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0] and grid[0][2] != '.':
        if grid[0][2] == '0':
            print('COMPUTER WON!')
        else:
            print('PLAYER WON!')
        return True

    for i in range(3):
        if grid[0][i] == grid[1][i] and grid[0][i] == grid[2][i] and grid[0][i] != '.':
            if grid[0][i] == '0':
                print('COMPUTER WON!')
            else:
                print('PLAYER WON!')
            return True


    count = 0
    for i in range(3):
        for x in range(3):
            if grid[i][x] == '.':
                count += 1

    if count == 0:
        print("Match Drawn.")
        return True
    return False

def generate_move(moves):
    return random.choice(moves)

def main():
    ch = int(input("If you would like to go first, press 0.  If you would like the computer to go first, press 1. Make your selection here: "))
    grid = [['.', '.','.'], ['.', '.','.'], ['.', '.','.']]
    moves = []
    for i in range(3):
        for x in range(3):
            moves.append((i,x))

    turn = 0

    while(not win_or_draw(grid)):
        print_grid(grid)
        player = "PLAYER" if turn == ch else "COMPUTER"
        print("Turn: %s" % (player))

        if turn == ch:
            a, b = map(int, input().strip().split())
            moves.remove((a,b))
        else:
            a,b = generate_move(moves)
            moves.remove((a,b))
        grid[a][b] = 'X' if turn == ch else 'O'
        turn ^= 1

    print_grid(grid)

main()