import tkinter as tk
from tkinter import font

# Function to update the puzzle's state on the GUI
def update_puzzle(grid, state):
    for i in range(3):
        for j in range(3):
            grid[i][j].config(text=state[i][j])

# Function to generate the next state (example: using dummy states for demo purposes)
def next_state():
    global puzzle_states, current_state
    if current_state < len(puzzle_states):
        update_puzzle(puzzle_grid, puzzle_states[current_state])
        current_state += 1
    else:
        print("Reached goal state!")

# Initial state of the 8-puzzle (can be entered by the user)
initial_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # '0' represents the empty space

# Example goal states (you would replace this with the actual search algorithm)
puzzle_states = [
    [[1, 2, 3], [4, 5, 6], [7, 0, 8]],
    [[1, 2, 3], [4, 0, 6], [7, 5, 8]],
    [[1, 2, 3], [0, 4, 6], [7, 5, 8]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 0]],  # Goal state
]

current_state = 0

# Create a Tkinter window
root = tk.Tk()
root.title("8-Puzzle Game")
root.geometry("200x200")

# Create a grid for displaying the puzzle
puzzle_grid = []
for i in range(3):
    row = []
    for j in range(3):
        label = tk.Label(root, text=initial_state[i][j], width=5, height=2, font=("Helvetica", 24))
        label.grid(row=i, column=j)
        row.append(label)
    puzzle_grid.append(row)

# Button to move to the next state
next_button = tk.Button(root, text="Next State", command=next_state)
next_button.grid(row=4, column=1)

# Start the Tkinter event loop
root.mainloop()
