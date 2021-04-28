class Unit:
    NONE = 0
    X = 1
    O = 2

class GameState:
    TIE = -1
    RUNNING = 0
    X_WON = Unit.X
    O_WON = Unit.O

class GameData:
    def __init__(self, board, player_turn, game_state):
        self.board = board
        self.player_turn = player_turn
        self.game_state = game_state

    def default(n=3):
        """Generate a regular tic tac toe game with a board size n * n"""
        board = []
        for _ in range(n):
            board.append([Unit.NONE] * n)
        return GameData(board, Unit.X, GameState.RUNNING)

    def play(self, row, column):
        """Plays a turn at a position. (0, 0) = top left. Returns Game State"""
        self.board[row][column] = self.player_turn
        if self.won():
            self.game_state = self.player_turn
        if self.filled():
            self.game_state = GameState.TIE
        self.player_turn = Unit.X if self.player_turn == Unit.O else Unit.O
        return self.game_state

    def filled(self):
        for row in self.board:
            for x in row:
                if x == Unit.NONE:
                    return False
        return True

    def won(self):
        def horizonal():
            for row in self.board:
                if row == [self.player_turn] * len(self.board):
                    return True
            return False
        def vertical():
            streaks = [0] * len(self.board)
            for row in self.board:
                for i, x in enumerate(row):
                    if x == self.player_turn:
                        streaks[i] += 1
            for streak in streaks:
                if streak == len(self.board):
                    return True
            return False
        def diagonal():
            up = 0
            down = 0
            board_len = len(self.board)
            for i in range(board_len):
                if self.board[i][i] == self.player_turn:
                    down += 1
                if self.board[board_len - i - 1][board_len - i - 1] == self.player_turn:
                    up += 1
            if up == board_len or down == board_len:
                return True
   
        return diagonal() or horizonal() or vertical()

#
#    a     b     c
#       |     |
# 1  -  |  -  |  -
#  _____|_____|_____
#       |     |
# 2  -  |  -  |  -
#  _____|_____|_____
#       |     |
# 3  -  |  -  |  -
#       |     |
#
def render(game_data):
    def header():
        return "".join([f"     {chr(n + ord('a'))}" for n in range(len(game_data.board))])[1:]
    def bars():
        string = "       |"
        for i in range(len(game_data.board) - 1):
            string += "     |"
        return string[:-1]
    def underline():
        string = "  _____|"
        for i in range(len(game_data.board) - 1):
            string += "_____|"
        return string[:-1]
    def unit(u):
        if u == Unit.X:
            return 'X'
        if u == Unit.O:
            return "O"
        else:
            return "-"

    print()
    print(header())
    for row_num, row in enumerate(game_data.board):
        print(bars())
        print(f" {row_num + 1}", end="")
        for x_num, x in enumerate(row):
            if x_num != 0:
                print("|", end="")
            print(f"  {unit(x)}  ", end="")
        print()
        if row_num != len(game_data.board) - 1:
            print(underline())
        else:
            print(bars())
    print()


def get_size():
    try:
        size = int(input("Enter board size: "))
    except:
        print("Invalid input. Board size has to be a number.")
        return get_size()
    if size < 3 or size > 9:
        print("Invalid input. Board size has to be between 3 and 9.")
        return get_size()
    return size

def get_input(game_data):
    def alpha_exists(c):
        return c[0].isalpha() or c[1].isalpha()
    def number_exists(c):
        return c[0].isnumeric() or c[1].isnumeric()
    name = "Player " + ("1" if game_data.player_turn == Unit.X else "2")
    coord = input(f"{name}, enter coordinates: ")
    if len(coord) != 2 or not alpha_exists(coord) or not number_exists(coord):
        print("Invalid input. Coordinates must contain one letter and one number. Ex. 3a")
        return get_input(game_data)
    return coord

# Assumes input is valid
def parse_input(coord_str):
    def get_letter_and_num():
        if coord_str[0].isalpha():
            return coord_str[0], coord_str[1]
        else:
            return coord_str[1], coord_str[0]
    x, y = get_letter_and_num()
    return ord(x) - ord('a'), int(y) - 1

def play_turn(game, row, col):
    size = len(game.board)
    if row >= size or col >= size or col < 0 or row < 0:
        print("Invalid input. Position is not within the board.")
        return False, GameState.RUNNING
    if game.board[row][col] != Unit.NONE:
        print("Invalid input. Position already taken.")
        return False, GameState.RUNNING
    return True, game.play(row, col)

def main():
    game = GameData.default(get_size())
    state = GameState.RUNNING
    while state == GameState.RUNNING:
        render(game)
        succeed = False
        while not succeed:
            col, row = parse_input(get_input(game))
            succeed, state = play_turn(game, row, col)
    render(game)
    if state == GameState.X_WON:
        print("X Won!")
    elif state == GameState.O_WON:
        print("O Won!")
    else:
        print("TIE!")
main()
