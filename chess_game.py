class Rook:
    def __init__(self, color):
        self.color = color

    def get_possible_moves(self, current_row, current_col, board):
        possible_moves = []

        # Движение вверх
        for row in range(current_row - 1, -1, -1):
            if board[row][current_col] == ' ':
                possible_moves.append((row, current_col))
            else:
                if board[row][current_col].color != self.color:
                    possible_moves.append((row, current_col))
                break

        # Движение вниз
        for row in range(current_row + 1, 8):
            if board[row][current_col] == ' ':
                possible_moves.append((row, current_col))
            else:
                if board[row][current_col].color != self.color:
                    possible_moves.append((row, current_col))
                break

        # Движение влево
        for col in range(current_col - 1, -1, -1):
            if board[current_row][col] == ' ':
                possible_moves.append((current_row, col))
            else:
                if board[current_row][col].color != self.color:
                    possible_moves.append((current_row, col))
                break

        # Движение вправо
        for col in range(current_col + 1, 8):
            if board[current_row][col] == ' ':
                possible_moves.append((current_row, col))
            else:
                if board[current_row][col].color != self.color:
                    possible_moves.append((current_row, col))
                break

        return possible_moves



class Pawn:
    def __init__(self, color):
        self.color = color

    def get_possible_moves(self, current_row, current_col, board):
        possible_moves = []
        if self.color == 'white':
            # Пешка белого цвета может двигаться вперед на одну клетку
            if current_row - 1 >= 0 and board[current_row - 1][current_col] == ' ':
                possible_moves.append((current_row - 1, current_col))

            # Пешка белого цвета может двигаться вперед на две клетки, если она находится на начальной позиции
            if current_row == 6 and board[current_row - 1][current_col] == ' ' and board[current_row - 2][
                current_col] == ' ':
                possible_moves.append((current_row - 2, current_col))

            # Пешка белого цвета может двигаться по диагонали, чтобы съесть фигуру другого цвета
            if current_row - 1 >= 0 and current_col - 1 >= 0 and board[current_row - 1][current_col - 1] != ' ':
                possible_moves.append((current_row - 1, current_col - 1))
            if current_row - 1 >= 0 and current_col + 1 <= 7 and board[current_row - 1][current_col + 1] != ' ':
                possible_moves.append((current_row - 1, current_col + 1))
        else:
            # Пешка черного цвета может двигаться вперед на одну клетку
            if current_row + 1 <= 7 and board[current_row + 1][current_col] == ' ':
                possible_moves.append((current_row + 1, current_col))

            # Пешка черного цвета может двигаться вперед на две клетки, если она находится на начальной позиции
            if current_row == 1 and board[current_row + 1][current_col] == ' ' and board[current_row + 2][
                current_col] == ' ':
                possible_moves.append((current_row + 2, current_col))

            # Пешка черного цвета может двигаться по диагонали, чтобы съесть фигуру другого цвета
            if current_row + 1 <= 7 and current_col - 1 >= 0 and board[current_row + 1][current_col - 1] != ' ':
                possible_moves.append((current_row + 1, current_col - 1))
            if current_row + 1 <= 7 and current_col + 1 <= 7 and board[current_row + 1][current_col + 1] != ' ':
                possible_moves.append((current_row + 1, current_col + 1))

        return possible_moves


class King:
    def __init__(self, color):
        self.color = color

    def get_possible_moves(self, current_row, current_col, board):
        possible_moves = []

        # Все возможные направления ходов короля
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for direction in directions:
            row = current_row + direction[0]
            col = current_col + direction[1]

            if row >= 0 and row < 8 and col >= 0 and col < 8:
                if board[row][col] == ' ':
                    possible_moves.append((row, col))
                elif board[row][col].color != self.color:
                    possible_moves.append((row, col))

        return possible_moves



class Knight:
    def __init__(self, color):
        self.color = color

    def get_possible_moves(self, current_row, current_col, board):
        possible_moves = []

        # Возможные относительные смещения для ходов коня
        moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

        for move in moves:
            row = current_row + move[0]
            col = current_col + move[1]

            if row >= 0 and row < 8 and col >= 0 and col < 8:
                if board[row][col] == ' ':
                    possible_moves.append((row, col))
                else:
                    target_piece = board[row][col]
                    if target_piece.color != self.color:
                        possible_moves.append((row, col))

        return possible_moves



class Bishop:
    def __init__(self, color):
        self.color = color

    def get_possible_moves(self, current_row, current_col, board):
        possible_moves = []

        # Движение по диагонали вверх-влево
        row, col = current_row - 1, current_col - 1
        while row >= 0 and col >= 0:
            if board[row][col] == ' ':
                possible_moves.append((row, col))
            else:
                if board[row][col].color != self.color:
                    possible_moves.append((row, col))
                break
            row -= 1
            col -= 1

        # Движение по диагонали вверх-вправо
        row, col = current_row - 1, current_col + 1
        while row >= 0 and col < 8:
            if board[row][col] == ' ':
                possible_moves.append((row, col))
            else:
                if board[row][col].color != self.color:
                    possible_moves.append((row, col))
                break
            row -= 1
            col += 1

        # Движение по диагонали вниз-влево
        row, col = current_row + 1, current_col - 1
        while row < 8 and col >= 0:
            if board[row][col] == ' ':
                possible_moves.append((row, col))
            else:
                if board[row][col].color != self.color:
                    possible_moves.append((row, col))
                break
            row += 1
            col -= 1

        # Движение по диагонали вниз-вправо
        row, col = current_row + 1, current_col + 1
        while row < 8 and col < 8:
            if board[row][col] == ' ':
                possible_moves.append((row, col))
            else:
                if board[row][col].color != self.color:
                    possible_moves.append((row, col))
                break
            row += 1
            col += 1

        return possible_moves



class Queen:
    def __init__(self, color):
        self.color = color

    def get_possible_moves(self, current_row, current_col, board):
        possible_moves = []

        # Движение вверх
        for row in range(current_row - 1, -1, -1):
            if board[row][current_col] == ' ':
                possible_moves.append((row, current_col))
            else:
                if board[row][current_col].color != self.color:
                    possible_moves.append((row, current_col))
                break

        # Движение вниз
        for row in range(current_row + 1, 8):
            if board[row][current_col] == ' ':
                possible_moves.append((row, current_col))
            else:
                if board[row][current_col].color != self.color:
                    possible_moves.append((row, current_col))
                break

        # Движение влево
        for col in range(current_col - 1, -1, -1):
            if board[current_row][col] == ' ':
                possible_moves.append((current_row, col))
            else:
                if board[current_row][col].color != self.color:
                    possible_moves.append((current_row, col))
                break

        # Движение вправо
        for col in range(current_col + 1, 8):
            if board[current_row][col] == ' ':
                possible_moves.append((current_row, col))
            else:
                if board[current_row][col].color != self.color:
                    possible_moves.append((current_row, col))
                break

        # Движение по диагонали вверх-влево
        row, col = current_row - 1, current_col - 1
        while row >= 0 and col >= 0:
            if board[row][col] == ' ':
                possible_moves.append((row, col))
            else:
                if board[row][col].color != self.color:
                    possible_moves.append((row, col))
                break
            row -= 1
            col -= 1

        # Движение по диагонали вверх-вправо
        row, col = current_row - 1, current_col + 1
        while row >= 0 and col < 8:
            if board[row][col] == ' ':
                possible_moves.append((row, col))
            else:
                if board[row][col].color != self.color:
                    possible_moves.append((row, col))
                break
            row -= 1
            col += 1

        # Движение по диагонали вниз-влево
        row, col = current_row + 1, current_col - 1
        while row < 8 and col >= 0:
            if board[row][col] == ' ':
                possible_moves.append((row, col))
            else:
                if board[row][col].color != self.color:
                    possible_moves.append((row, col))
                break
            row += 1
            col -= 1

        # Движение по диагонали вниз-вправо
        row, col = current_row + 1, current_col + 1
        while row < 8 and col < 8:
            if board[row][col] == ' ':
                possible_moves.append((row, col))
            else:
                if board[row][col].color != self.color:
                    possible_moves.append((row, col))
                break
            row += 1
            col += 1

        return possible_moves



class ChessGame:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.initialize_pieces()

    def initialize_pieces(self):
        # Расстановка фигур на доске
        self.board[0][0] = Rook('black')
        self.board[0][1] = Knight('black')
        self.board[0][2] = Bishop('black')
        self.board[0][3] = Queen('black')
        self.board[0][4] = King('black')
        self.board[0][5] = Bishop('black')
        self.board[0][6] = Knight('black')
        self.board[0][7] = Rook('black')

        self.board[7][0] = Rook('white')
        self.board[7][1] = Knight('white')
        self.board[7][2] = Bishop('white')
        self.board[7][3] = Queen('white')
        self.board[7][4] = King('white')
        self.board[7][5] = Bishop('white')
        self.board[7][6] = Knight('white')
        self.board[7][7] = Rook('white')

        for col in range(8):
            self.board[1][col] = Pawn('black')
            self.board[6][col] = Pawn('white')

    def move_piece(self, start_pos, end_pos):
        # Convert start position from alphanumeric to indices
        start_col = ord(start_pos[0].upper()) - ord('A')
        start_row = 8 - int(start_pos[1])

        # Convert end position from alphanumeric to indices
        end_col = ord(end_pos[0].upper()) - ord('A')
        end_row = 8 - int(end_pos[1])

        # Check valid starting position
        if (
            start_row < 0 or start_row > 7 or
            start_col < 0 or start_col > 7 or
            self.board[start_row][start_col] == ' '
        ):
            print("Invalid starting position.")
            return

        piece = self.board[start_row][start_col]

        # Determine player color
        player_color = piece.color

        # Check if move is valid for the selected piece
        possible_moves = piece.get_possible_moves(start_row, start_col, self.board)
        if (end_row, end_col) not in possible_moves:
            print("Invalid move for the selected piece.")
            return

        target_piece = self.board[end_row][end_col]

        # Check if the target position is occupied by a piece of the opposite color
        if target_piece != ' ':
            if target_piece.color != player_color:
                print(f"Captured {target_piece.color} {type(target_piece).__name__} at {end_pos}.")
                self.board[end_row][end_col] = piece
                self.board[start_row][start_col] = ' '
            else:
                print("Invalid move. Target position is occupied by your own piece.")
                return

        # Move the piece
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = ' '

        print(f"Moved {player_color} {type(piece).__name__} from {start_pos} to {end_pos}.")
        


    



    def print_board(self):
        # Print column labels
        print('  A B C D E F G H')

        # Print rows with pieces
        for i, row in enumerate(self.board):
            # Print row number
            print(f'{8 - i} ', end='')

            for square in row:
                if square == ' ':
                    print('.', end=' ')
                else:
                    piece = square
                    if piece.color == 'white':
                        print(piece.__class__.__name__[0].upper(), end=' ')
                    else:
                        print(piece.__class__.__name__[0].lower(), end=' ')

            # Print row number again
            print(f' {8 - i}')

        # Print column labels
        print('  A B C D E F G H')


def get_player_input(game):
    players = ['black', 'white']
    player_index = 0

    while True:
        game.print_board()
        print()
        # Get the current player's color
        player_color = players[player_index]

        # Ask for input
        print(f"{player_color} player's turn:")
        start = input("Enter the starting position (e.g., a5): ")
        end = input("Enter the ending position (e.g., a6): ")

        # Process the input
        if start.lower() == 'exit' or end.lower() == 'exit':
            break  # Exit the loop if the player enters 'exit'
        else:
            # Make the move
            game.move_piece(start, end)

            # Print the updated board
            game.print_board()

            # Switch to the next player
            player_index = (player_index + 1) % 2


Game = ChessGame()

get_player_input(Game)