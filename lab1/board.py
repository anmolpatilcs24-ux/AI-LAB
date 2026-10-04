def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print()


def check_winner(board):
    # Rows
    for row in board:
        if row[0] != '-' and row[0] == row[1] == row[2]:
            return row[0]

    # Columns
    for col in range(3):
        if (board[0][col] != '-' and
                board[0][col] == board[1][col] == board[2][col]):
            return board[0][col]

    # Diagonals
    if board[0][0] != '-' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] != '-' and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


def is_terminal(board):
    # Someone won
    if check_winner(board) is not None:
        return True

    # Board is full
    for row in board:
        if '-' in row:
            return False

    return True


def get_empty_cells(board):
    """Return all empty positions."""
    empty = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                empty.append((i, j))

    return empty


def make_move(board, position, player):
    """Create a new board after making a move."""
    new_board = [row[:] for row in board]

    i, j = position
    new_board[i][j] = player

    return new_board


def determine_player(board):
    """
    Determine whose turn it is.

    X starts the game.
    If X and O have made the same number of moves -> X's turn.
    Otherwise -> O's turn.
    """

    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)

    if x_count == o_count:
        return 'X'
    else:
        return 'O'


# state safe search

def brute_force(board, player, path_cost, path):
    """
    Explore every possible continuation from the given state.

    Each move has a cost of 1.

    path_cost = total number of moves made
                after the user's initial board.
    """

    # Store current state in path
    path.append([row[:] for row in board])

    # If game is over, print the result
    if is_terminal(board):

        winner = check_winner(board)

        print("\n==============================")
        print("TERMINAL STATE")
        print("==============================")

        print_board(board)

        if winner:
            print("Winner:", winner)
        else:
            print("Result: DRAW")

        print("Path Cost:", path_cost)

        print("\nPath:")
        for step, state in enumerate(path):
            print("\nStep", step, "(Cost =", step, ")")
            print_board(state)

        path.pop()
        return

    # Generate every possible next move
    empty_cells = get_empty_cells(board)

    for position in empty_cells:

        # Make move
        new_board = make_move(board, position, player)

        # Every move costs 1
        new_cost = path_cost + 1

        # Switch player
        next_player = 'O' if player == 'X' else 'X'

        # Recursively explore
        brute_force(
            new_board,
            next_player,
            new_cost,
            path
        )

    path.pop()

# user input
print("TIC-TAC-TOE BRUTE FORCE STATE SPACE")
print("------------------------------------")

print("\nEnter the partially filled board.")
print("Use X, O and - for empty cells.\n")

board = []

for i in range(3):

    while True:

        row = input(
            f"Enter row {i + 1} "
            "(example: X O -): "
        ).upper().split()

        if len(row) != 3:
            print("Please enter exactly 3 values.")
            continue

        if all(cell in ['X', 'O', '-'] for cell in row):
            board.append(row)
            break

        print("Use only X, O and -.")


#/search
print("\nInitial State:")
print_board(board)

# Determine whose turn it is
player = determine_player(board)

print("Next player:", player)

print("\nStarting brute-force state-space search...")

brute_force(
    board,
    player,
    0,
    []
)
