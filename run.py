from src.board import Board

b = Board(available_letters=['T', 'S', 'O', 'W', 'U', 'I', 'R'])
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

def is_ok_direction(current, next, horizontal=True):
    if horizontal:
        return next[0] == current[0] and abs(next[1] - current[1]) == 1
    return next[1] == current[1] and abs(next[0] - current[0]) == 1

def find_best_word(board):
    letter_length = random.randint(1, len(board.available_letters))
    tile = random.choice(b.get_valid_placement_tiles())
    direction = random.randint(0, 1)
    letters = random.sample(board.available_letters, letter_length)
    letter_index = 0
    print("Choosing ", letter_length, "letters is horizontal : ", direction==HORIZONTAL)
    while letter_index < len(letters):
        if tile:
            board.grid[tile[0]][tile[1]] = letters[letter_index]
            print("Placed %s" % letters[letter_index], tile)
            row_valid_tiles = [tt for tt in b.get_valid_placement_tiles() if is_ok_direction(tile, tt, horizontal=direction==HORIZONTAL)]
        if len(row_valid_tiles) > 0:
            tile = random.choice(row_valid_tiles)
            letter_index += 1
        else:
            break


find_best_word(b)