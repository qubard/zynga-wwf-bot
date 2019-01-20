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