from src.board import Board

b = Board(available_letters=['U',  'I', 'R', 'B', 'I', 'O'], \
          word_set=set(open("wordlist.txt", "r+").read().split('\n')))
b.add_word("VIP", (5,4))
b.add_word("PEHS", (5,6), horizontal=False)
b.add_word("YEAH", (7,3))
b.add_word("GANE", (8,0))
b.add_word("TOWS", (9,1))
b.add_word("O", (10,2))
b.add_word("SELFS", (8,6))
b.add_word("TAE", (9,7))
b.add_word("KARN", (10,6))
print(b)

print(b.words_at((8,0)))
print(b.words_at((8,1)))
print(b.words_at((8,2)))
print(b.words_at((8,3)))
print(b.words_at((9,3)))
print(b.words_at((10,2)))
print(b.words_at((0,0)))
print(b.words_at((9,3)))
print(b.words_at((6,6)))

print(b.words_at((8,6)))
print(b.words_at((7,6)))

"""
('GANE', None)
('GANE', 'AT')
('GANE', 'NOO')
('GANE', 'YEW')
('TOWS', 'YEW')
(None, 'NOO')
(None, None)
('TOWS', 'YEW')
(None, 'PEHS')
('SELFS', 'PEHS')
('YEAH', 'PEHS')
"""

print(b.get_valid_placement_tiles())

import random

HORIZONTAL = 0


def is_ok_direction(board, current, next, horizontal=True):
    dx = 0
    dy = 0
    delta = next[1] - current[1]
    if horizontal:
        dx = -1
        if next[1] > current[1]:
            dx = 1
    else:
        delta = next[0] - current[0]
        dy = -1
        if next[0] > current[0]:
            dy = 1
    valid = True
    for i in range(0, abs(delta)):
        if board.grid[current[0] + dy * i][current[1] + dx * i] == " ":
            valid = False
    if horizontal:
        return next[0] == current[0] and valid
    return next[1] == current[1] and valid

def find_best_word(board):
    letter_length = random.randint(1, len(board.available_letters))
    valid_tiles = board.get_valid_placement_tiles()
    if valid_tiles is None or len(valid_tiles) == 0:
        return False

    tile = random.choice(valid_tiles)
    direction = random.randint(0, 1)
    letters = random.sample(board.available_letters, letter_length)
    letter_index = 0
    tiles = []
    word = ""

    while letter_index < len(letters):
        if tile:
            board.grid[tile[0]][tile[1]] = letters[letter_index]
            word += letters[letter_index]
            tiles.append(tile)
            row_valid_tiles = [tt for tt in board.get_valid_placement_tiles() if \
                               is_ok_direction(board, tile, tt, horizontal=direction==HORIZONTAL)]
        if len(row_valid_tiles) > 0:
            tile = random.choice(row_valid_tiles)
            letter_index += 1
        else:
            break

    for tile in tiles:
        if not board.valid_word(tile):
            return False

    return word

seen_boards = set()

for _ in range(0, 100000):
    prevgrid = b.get_grid()
    word = find_best_word(b)
    if word:
        hash = b.hash()
        if hash not in seen_boards:
            seen_boards.add(hash)
            print(b, hash, word)
    b.set_grid(prevgrid)