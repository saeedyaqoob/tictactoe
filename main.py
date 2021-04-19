# Function to print the whole board with a positioning board for reference
def print_table(board):
    print(f'| {board["00"]} | {board["01"]} | {board["02"]} |       | 00 | 01 | 02 |\n'
          f'| {board["10"]} | {board["11"]} | {board["12"]} |       | 10 | 11 | 12 |\n'
          f'| {board["20"]} | {board["21"]} | {board["22"]} |       | 20 | 21 | 22 |\n')


# Function to check if the board is full
def fill(board):
    count = len(board)
    for key in board:
        if board[key] != ' ':
            count -= 1
    if count == 0:
        return True


# Function to check if there is a winner
def win(player):
    global table
    if (table['00'] == table['01'] == table['02'] == player) or (
            table['10'] == table['11'] == table['12'] == player) or (
            table['20'] == table['21'] == table['22'] == player) or (
            table['00'] == table['10'] == table['20'] == player) or (
            table['01'] == table['11'] == table['21'] == player) or (
            table['02'] == table['12'] == table['22'] == player) or (
            table['00'] == table['11'] == table['22'] == player) or (
            table['02'] == table['11'] == table['20'] == player):
        return True
    else:
        return False


# Function to mark a choice
def chance(name, marker):
    global table
    position = input(f'{name}, enter your position: ')
    if table[position] == ' ':
        table[position] = marker
    else:
        while table[position] != ' ':
            position = input(f'Position already taken!\n{name}, enter your position: ')
        table[position] = marker
    print_table(table)
    if win(marker):
        print(f'{name} is the Winner.')
        return True
    elif fill(table):
        print("It's a DRAW.")
        return True


# Dictionary of board choices/positions
table = {
    '00': ' ', '01': ' ', '02': ' ',
    '10': ' ', '11': ' ', '12': ' ',
    '20': ' ', '21': ' ', '22': ' '
}

print_table(table)

player_1 = input('Player1, choose your mark: X or O: ').upper()

if player_1 == 'X':
    player_2 = 'O'
else:
    player_2 = 'X'

while True:
    if chance(name='Player1', marker=player_1):
        break
    if chance(name='Player2', marker=player_2):
        break
