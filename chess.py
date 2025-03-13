#!/usr/bin/env python3
# Simple Chess Game Without Any Library
# Only Supports Basic Moves - No Castling, No En Passant, No Checkmate Detection

# Initialize the board as a 2D list
board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

# Mapping from letters to board indices
files = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

def print_board():
    """Prints the chessboard."""
    print("\n    a b c d e f g h")
    print("    ----------------")
    for i in range(8):
        print(8 - i, "|", " ".join(board[i]), "|", 8 - i)
    print("    ----------------")
    print("    a b c d e f g h\n")

def is_valid_move(start, end, turn):
    """Checks if a move is valid (very basic rule implementation)."""
    x1, y1 = start
    x2, y2 = end
    piece = board[x1][y1]
    
    if piece == ".":
        return False  # No piece at start position

    # Ensure players move their own pieces
    if (turn == "White" and piece.islower()) or (turn == "Black" and piece.isupper()):
        return False

    # Check movement rules for each piece
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    
    # Pawn Movement (does not handle captures)
    if piece.lower() == "p":
        direction = -1 if piece.isupper() else 1  # White moves up, Black moves down
        if y1 == y2 and (x2 - x1) == direction and board[x2][y2] == ".":
            return True  # Normal move
        if y1 == y2 and (x2 - x1) == 2 * direction and (x1 == 1 or x1 == 6) and board[x2][y2] == ".":
            return True  # Double move

    # Rook Movement
    elif piece.lower() == "r":
        if x1 == x2 or y1 == y2:
            return True

    # Bishop Movement
    elif piece.lower() == "b":
        if dx == dy:
            return True

    # Queen Movement
    elif piece.lower() == "q":
        if dx == dy or x1 == x2 or y1 == y2:
            return True

    # King Movement (no castling)
    elif piece.lower() == "k":
        if dx <= 1 and dy <= 1:
            return True

    # Knight Movement
    elif piece.lower() == "n":
        if (dx, dy) in [(2, 1), (1, 2)]:
            return True

    return False

def get_coordinates(move):
    """Converts algebraic notation (e2 e4) to board indices."""
    try:
        start, end = move.split()
        return (8 - int(start[1]), files[start[0]]), (8 - int(end[1]), files[end[0]])
    except (IndexError, KeyError, ValueError):
        return None, None

def play_chess():
    """Main game loop for chess."""
    turn = "White"
    while True:
        print_board()
        move = input(f"{turn}'s Move (e.g., e2 e4, or 'q' to quit): ").strip().lower()
        if move == "q":
            print("Game Over.")
            break

        start, end = get_coordinates(move)
        if start and end and is_valid_move(start, end, turn):
            board[end[0]][end[1]] = board[start[0]][start[1]]
            board[start[0]][start[1]] = "."
            turn = "Black" if turn == "White" else "White"  # Switch turn
        else:
            print("Invalid move. Try again.")

# Start the game
play_chess()
