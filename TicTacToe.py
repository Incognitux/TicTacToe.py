#  A two player turn-based Tic-Tac-Toe game

import time
import sys

row1 = ["a1", "b1", "c1"]
row2 = ["a2", "b2", "c2"]
row3 = ["a3", "b3", "c3"]
inputX = "X"
inputO = "O"

rows = [row1, row2, row3]
coord_to_indices = {
                    "a1": (0, 0), "b1": (0, 1), "c1": (0, 2),
                    "a2": (1, 0), "b2": (1, 1), "c2": (1, 2),
                    "a3": (2, 0), "b3": (2, 1), "c3": (2, 2),
                    }
all_coords = ["a1", "b1", "c1", "a2", "b2", "c2", "a3", "b3", "c3"]
occupied_coords = []

# dialogues
dialogue_invalid = "\nINVALID COORDINATE, TRY AGAIN."
dialogue_occupied = "\nCOORDINATE OCCUPIED, TRY A DIFFERENT COORDINATE."
dialogue_win = "\nTHE WINNER IS PLAYER"
dialogue_draw = "\nGAME DRAW, YOU BOTH LOSE"


def spacer(symbol):
    for i in range(26):
        time.sleep(0.03)
        sys.stdout.write(symbol)
        sys.stdout.flush()
    print("")


# define a function to print the board
def print_board():
    for board in rows:
        print("")
        print(board)
        print("")


# define a function to check winner
def check_winner():
    for row in rows:
        if row[0] == row[1] == row[2]:
            return row[0]

    for column in range(3):
        if rows[0][column] == rows[1][column] == rows[2][column]:
            return rows[0][column]

    # diagonals
    if rows[0][0] == rows[1][1] == rows[2][2]:
        return rows[0][0]
    if rows[0][2] == rows[1][1] == rows[2][0]:
        return rows[0][2]


# Game commence
print_board()
# Player X's turn
while True:
    playerInputX = input("Player X's turn,\n"+"Enter coordinate: ")
    if playerInputX not in coord_to_indices:
        print(dialogue_invalid)
        continue
    if playerInputX in occupied_coords:
        print(dialogue_occupied)
        continue
    row_index, col_index = coord_to_indices[playerInputX]
    rows[row_index][col_index] = inputX

    occupied_coords.append(playerInputX)

    winner = check_winner()
    if winner:
        print(dialogue_win, winner+"!")
        spacer(inputX)
        break

    # check game draw
    if len(occupied_coords) == len(all_coords):
        print(dialogue_draw)
        spacer("=")
        break
    spacer("_")
    print_board()


# Player O's turn
    while True:
        playerInputO = input("Player O's turn,\n"+"Enter coordinate: ")
        if playerInputO not in coord_to_indices:
            print(dialogue_invalid)
            continue
        if playerInputO in occupied_coords:
            print(dialogue_occupied)
            continue
        else:
            break
    row_index, col_index = coord_to_indices[playerInputO]
    rows[row_index][col_index] = inputO

    occupied_coords.append(playerInputO)

    winner = check_winner()
    if winner:
        print(dialogue_win, winner+"!\n")
        spacer(inputO)
        break

    # check game draw
    if len(occupied_coords) == len(all_coords):
        print(dialogue_draw)
        spacer("=")
        break
    spacer("_")
    print_board()

time.sleep(1)
print("Final Board:")
print_board()
time.sleep(2)
print("Order of moves: ", occupied_coords)
