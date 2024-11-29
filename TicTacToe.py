# Tic-Tac-Toe Game with AI using Minimax Algorithm

def display_board(board):
    """Display the current state of the board."""
    for row in board:
        print(' | '.join(row))
        print('-' * 9)


def check_winner(board):
    """Check if there is a winner or a draw."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '_':
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '_':
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        return board[0][2]
    # Check draw
    if all(board[i][j] != '_' for i in range(3) for j in range(3)):
        return "Draw"
    return None


def minimax(board, depth, is_maximizing):
    """Implement the Minimax algorithm for optimal AI decision-making."""
    result = check_winner(board)
    if result == 'X':  # AI wins
        return 10 - depth
    elif result == 'O':  # Human wins
        return depth - 10
    elif result == "Draw": 
        return 0

    if is_maximizing:  # AI's turn
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = '_'
                    best_score = max(best_score, score)
        return best_score
    else:  # Human's turn
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = '_'
                    best_score = min(best_score, score)
        return best_score


def ai_move(board):
    """Determine the AI's move using the Minimax algorithm."""
    best_score = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = '_'
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


def user_move(board):
    """Get the user's move with input validation."""
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column: 0, 1, 2): ").split())
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '_':
                return (row, col)
            else:
                print("Cell already taken or invalid! Try again.")
        except ValueError:
            print("Invalid input! Enter two numbers separated by a space (e.g., 0 1).")


def main():
    """Main function to run the Tic-Tac-Toe game."""
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O' and the AI is 'X'.")
    
    board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]

    display_board(board)
    
    while True:
        print("Your turn!")
        row, col = user_move(board)
        board[row][col] = 'O'
        display_board(board)
        winner = check_winner(board)
        if winner:
            break

        print("AI's turn!")
        move = ai_move(board)
        board[move[0]][move[1]] = 'X'
        display_board(board)
        winner = check_winner(board)
        if winner:
            break
    if winner == "Draw":
        print("It's a draw!")
    else:
        print(f"{winner} wins!")


if __name__ == "__main__":
    main()
