import tkinter as tk
from tkinter import messagebox

def check_winner(board):
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]  # Diagonal
    ]

    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != " ":
            if board[pos[0]] == 'X':
                return 1 
            elif board[pos[0]] == 'O':
                return -1 

    return 0  


def minimax(curDepth, maxTurn, board):
    score = check_winner(board)
    if score == 1:
        return score - curDepth
    elif score == -1:
        return score + curDepth
    elif " " not in board:
        return 0

    if maxTurn:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board_copy = board[:]
                board_copy[i] = 'O'
                score = minimax(curDepth + 1, False, board_copy)
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board_copy = board[:]
                board_copy[i] = 'X'
                score = minimax(curDepth + 1, True, board_copy)
                best_score = min(best_score, score)
        return best_score


def computer_turn():
    global current_player
    best_move = None
    best_score = float('-inf')
    
    for i in range(9):
        if board[i] == ' ':
            board_copy = board[:]
            board_copy[i] = 'O'
            score = minimax(0, False, board_copy)
            
            if score == -1:  
                board[i] = 'O'
                buttons[i].config(text='O')
                if check_winner(board) != 0:
                    messagebox.showinfo("Winner!", f"Player AI wins!")
                    reset_board()
                return
            
       
            board_copy[i] = 'X'  
            user_score = minimax(0, True, board_copy)
            if user_score == 1:  
                board[i] = 'O'
                buttons[i].config(text='O')
           
                return
          
            if score > best_score:
                best_score = score
                best_move = i


    if best_move is not None:
        board[best_move] = 'O'
        buttons[best_move].config(text='O')
      

        if check_winner(board) != 0:
            messagebox.showinfo("Winner!", f"Player AI wins!")
            reset_board()
        elif " " not in board:
            messagebox.showinfo("Draw!", "It's a draw!")
            reset_board()





def on_button_click(row, col):
    global current_player
    index = row * 3 + col
    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player, state="disabled", disabledforeground="black")
        if check_winner(board) != 0:
            messagebox.showinfo("Winner!", f"Player {current_player} wins!")
            reset_board()
        elif " " not in board:
            messagebox.showinfo("Draw!", "It's a draw!")
            reset_board()
        else:
            current_player = "X"  
            
            computer_turn()




def reset_board():
    global current_player
    current_player = "X"
    global board
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text=" ", state="normal")
    

root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"
board = [" " for _ in range(9)]

buttons = []
for i in range(3):
    for j in range(3):
        button = tk.Button(root, text=" ", font=("Arial", 24), width=5, height=2, bg="#ffffff", fg="#000000",
                           activebackground="#eeeeee", activeforeground="#000000",
                           command=lambda row=i, col=j: on_button_click(row, col))
        button.grid(row=i, column=j, padx=5, pady=5)
        buttons.append(button)


root.mainloop()
