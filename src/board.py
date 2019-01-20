EMPTY_TILE = " "


class Board:
    def __init__(self, available_letters):
        self.modifiers = {};
        self.grid =[[EMPTY_TILE for _ in range(11)] for _ in range(11)]
        self.available_letters = available_letters
        self.letter_values = {
            'A': 1,
            'G': 3,
            'Y': 3,
            'E': 1,
            'M': 4,
            'V': 5,
            'I': 1,
            'P': 4,
            'S': 1,
            'L': 2,
            'K': 5,
            'T': 1,
            'R': 1,
            'N': 2,
            'D': 2,
            'F': 4,
            'J': 10,
            'H': 3,
            'W': 4,
            'B': 4,
            'Q': 10,
            'Z': 10,
            'X': 8,
            'U': 2,
            'C': 4,
            'O': 1,
            '*': 0
        }
        self._assign_modifiers()

    def _assign_modifiers(self):
        self.modifiers[(0, 0)] = "TL"
        self.modifiers[(0, 2)] = "TW"
        self.modifiers[(0, 8)] = "TW"
        self.modifiers[(0, 9)] = "TL"

        self.modifiers[(1, 1)] = "DW"
        self.modifiers[(1, 5)] = "DW"
        self.modifiers[(1, 9)] = "TW"

        self.modifiers[(2, 0)] = "TW"
        self.modifiers[(2, 2)] = "DL"
        self.modifiers[(2, 4)] = "DL"
        self.modifiers[(2, 6)] = "DL"
        self.modifiers[(2, 8)] = "DL"
        self.modifiers[(2, 10)] = "TW"

        self.modifiers[(3, 3)] = "TL"
        self.modifiers[(3, 7)] = "TL"

        self.modifiers[(4, 2)] = "DL"
        self.modifiers[(4, 7)] = "DL"

        self.modifiers[(5, 1)] = "DW"
        self.modifiers[(5, 5)] = "DW"
        self.modifiers[(5, 9)] = "DW"

        self.modifiers[(6, 2)] = "DL"
        self.modifiers[(6, 8)] = "DL"

        self.modifiers[(7, 5)] = "TL"
        self.modifiers[(7, 9)] = "TL"

        self.modifiers[(8, 2)] = "DL"
        self.modifiers[(8, 6)] = "DL"
        self.modifiers[(8, 8)] = "DL"

        self.modifiers[(9, 1)] = "DW"
        self.modifiers[(9, 5)] = "DW"
        self.modifiers[(9, 9)] = "DW"

        self.modifiers[(10, 0)] = "TL"
        self.modifiers[(10, 2)] = "TW"
        self.modifiers[(10, 8)] = "TW"
        self.modifiers[(10, 10)] = "TL"

    def has_anyone_moved(self):
        return self.grid[5][5] != EMPTY_TILE

    def add_word(self, word, place, horizontal=True):
        dx = 1 if horizontal else 0
        dy = 1 if not horizontal else 0
        for i in range(0, len(word)):
            self.grid[place[0] + i * dy][place[1] + i * dx] = word[i]

    def words_at(self, place):
        return self.word_at_horizontal(place), self.word_at_vertical(place)

    def word_at_horizontal(self, place):
        word = ""
        start_index = 0
        end_index = len(self.grid[place[0]])

        if self.grid[place[0]][place[1]] == EMPTY_TILE:
            return None

        # Scan from right to left for a space
        for i in range(1, place[1] + 1):
            if self.grid[place[0]][place[1] - i] == EMPTY_TILE:
                start_index = place[1] - i + 1
                break

        # Scan from left to right for the final space (end of word)
        for i in range(place[1], end_index):
            if self.grid[place[0]][i] == EMPTY_TILE:
                end_index = i
                break

        if start_index == end_index or end_index - start_index <= 1:
            return None

        for i in range(start_index, end_index):
            word += self.grid[place[0]][i]

        return word

    def word_at_vertical(self, place):
        word = ""
        start_index = 0
        end_index = len(self.grid)

        if self.grid[place[0]][place[1]] == EMPTY_TILE:
            return None

        # Scan from bottom to top for a space
        for i in range(1, place[0] + 1):
            if self.grid[place[0] - i][place[1]] == EMPTY_TILE:
                start_index = place[0] - i + 1
                break

        # Scan from top to bottom for the final space (end of word)
        for i in range(place[0], end_index):
            if self.grid[i][place[1]] == EMPTY_TILE:
                end_index = i
                break

        if start_index == end_index or end_index - start_index <= 1:
            return None

        for i in range(start_index, end_index):
            word += self.grid[i][place[1]]

        return word

    def __repr__(self):
        s = ""
        for line in self.grid:
            s += str(line) + "\n"
        return s

    def get_valid_placement_tiles(self):
        valid_tiles = []
        for y in range(0, len(self.grid)):
            for x in range(0, len(self.grid[y])):
                if self.grid[y][x] == EMPTY_TILE and \
                        (self.grid[min(y + 1, len(self.grid) - 1)][x] != EMPTY_TILE or self.grid[y][min(x + 1, len(self.grid[y]) - 1)] != EMPTY_TILE \
                         or self.grid[max(0, y - 1)][x] != EMPTY_TILE or self.grid[y][max(0, x - 1)] != EMPTY_TILE):
                    valid_tiles.append((y, x))
        return valid_tiles


    def generate_valid_word_spots(self):
        for y in range(0, len(self.grid)):
            for x in range(0, len(self.grid[y])):
                # go down the grid
                foundWord = False
                # (start, end, length)
                for i in range(0, len(self.available_letters)):
                    if self.grid[y][x] != EMPTY_TILE and not foundWord:
                        foundWord = True
                    elif foundWord and self.grid[y][x] != " ":
                        pass


