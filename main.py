import os
import random
import threading
import time
from msvcrt import getch
from random import randint

space = ""
movement = ""
fall_list = list(range(18))
empty_line = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
board_height = 20
board = [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]

tetris_shapes = {
    "Iblockhor": "[][][][]",
    "Iblockver": "[]\n[]\n[]\n[]",
    "Jblock1": "[]\n[][][]",
    "Jblock2": "    []\n\r[][][]",
    "Jblock3": "[][]\n[]\n[]",
    "Jblock4": "[][]\n  []\n  []",
    "Jblock5": "[]\n[]\n[][]",
    "Jblock6": "  []\n  []\n[][]",
    "Jblock7": "[][][]\n[]",
    "Jblock8": "[][][]\n    []",
    "Oblock": "[][]\n[][]",
    "Sblock1": "  [][]\n[][]",
    "Sblock2": "[][]\n  [][]",
    "Sblock3": "[]\n[][]\n  []",
    "Sblock4": "  []\n[][]\n[]",
    "Tblock1": "  []\n[][][]",
    "Tblock2": "[][][]\n  []",
    "Tblock3": "[]\n[][]\n[]",
    "Tblock4": ["[]", "\n", "[]", "[]", "\n", "[]"]
}
lines = [board[0], board[1], board[2], board[3], board[4], board[5], board[6],
         board[7], board[8], board[9], board[10], board[11], board[12], board[13],
         board[14], board[15], board[16], board[17], board[18], board[19]]


def draw_screen():
    os.system('cls')
    print("\n\n")
    for row in range(len(board)):
        line = "| "

        for col in range(len(board[0])):
            character = convert_to_symbol(board[row][col])
            line += f" {character} "

        print(line + " |")
    time.sleep(0.5)


def game_loop():
    # run the main loop of the game, moves the blocks downwards, also keep score.
    t1 = threading.Thread(target=user_input)
    t2 = threading.Thread(target=draw_square_block)
    game_exit = False
    while not game_exit:

        # selected_shape = tetris_shape_select()
        selected_shape = "Oblock"
        if selected_shape == "Oblock":
            t1.start()
            t2.start()

        game_exit = True
    t1.join()
    t2.join()

    # return keep_score()


def tetris_shape_select():
    selected_shape = random.choice(list(tetris_shapes.keys()))
    return selected_shape


# def keep_score():
# adds 1 to a removed rows counter every time a row is removed and sets the score to that counter

# def write_score():
# write the score at the end of the game to a txt file
# game_loop()
def reset_line(line):
    board[line] = empty_line


def clear_screen():
    global space
    for line in lines:
        for space in line:
            if int(space) == 1:
                space = "0"
    return space


def user_input() -> None:
    global movement
    while True:
        key = ord(getch())
        if key == 27:  # ESC
            exit()
        elif key == 32:  # Space
            movement = "rotate"
            print('rotate')
            time.sleep(0.5)
            movement = ""
        elif key == 224:  # Special keys (arrows, f keys, ins, del, etc.)
            key = ord(getch())
            if key == 75:  # Left arrow
                movement = "left"
                print('left')
                time.sleep(0.5)
                movement = ""
            elif key == 77:  # Right arrow
                movement = "right"
                print('right')
                time.sleep(0.5)
                movement = ""


def convert_to_symbol(number):
    if int(number) == 0:
        return ' * '
    if int(number) == 1:
        return '[ ]'
    if int(number) == 2:
        return '[ ]'
    return "error"


def draw_square_block():
    block_height = 2
    starting_line1 = 0
    starting_line2 = 1
    j = 0
    starting_col = randint(1, 9)

    # Draw initial block
    for i in range(starting_col - 1, starting_col + 1):
        print(starting_col)
        lines[starting_line1][i] = "1"
        lines[starting_line2][i] = "1"

    draw_screen()

    # Move the block down step by step
    for _ in range(board_height-block_height):
        starting_line1 += 1
        starting_line2 += 1

        for j in range(starting_col - 1, starting_col + 1):
            print(starting_col)
            lines[starting_line1][j] = "1"
            lines[starting_line2][j] = "1"

        reset_line(starting_line1 - 1)
        draw_screen()
        if movement == "left" and starting_col > -1:
            starting_col -= 1

        if movement == "right" and starting_col < 9:
            starting_col += 1

        print("\n")

    # Make the block fixed
    lines[starting_line1][j] = "2"
    lines[starting_line2][j] = "2"
    # clear_screen()


def main():
    # draw_screen()
    # write_score()

    game_loop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
