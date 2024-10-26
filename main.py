from BFS import *
import tkinter as tk


def update_puzzle():
    global state, puzzle_grid
    state_list = number_to_state(state)
    for i in range(3):
        for j in range(3):
            puzzle_grid[i][j].config(text=state_list[i][j])


def next_state():
    global child, state
    if state != 12345678:
        state = child[state]
    update_puzzle()


def prev_state():
    global parent, state
    if parent[state] != -1:
        state = parent[state]
    update_puzzle()


while True:
    start = ""
    while start != "exit" and start != "game":
        print("Please enter game or exit.")
        start = input()
    if start == "exit":
        break
    initial_state = []
    while not enter_state(initial_state):
        print("invalid input, please enter the game in that form with different order\n0 1 2\n3 4 5\n6 7 8")
    initial_state = state_to_number(initial_state)
    if not solvable(initial_state):
        print("The puzzle can't be solved")
        continue
    choice = False
    child = {}
    parent = {}
    while not choice:
        choice = True
        print("Please choose algorithm enter:\n1 for BFS\n2 for DFS\n"
              "3 for iterative DFS\n4 for Manhattan A*\n5 for Euclidean A*")
        algorithm = input()
        match algorithm:
            case "1":
                parent, child = solve_bfs(initial_state)
            case "2":
                print("DFS")
            case "3":
                print("iterative DFS")
            case "4":
                print("Manhattan A*")
            case "5":
                print("Euclidean A*")
            case _:
                choice = False
    root = tk.Tk()
    root.title("8-Puzzle Game")
    root.geometry("250x250")

    state = initial_state
    initial_state = number_to_state(initial_state)
    puzzle_grid = []
    for i in range(3):
        row = []
        for j in range(3):
            label = tk.Label(root, text=initial_state[i][j], width=5, height=2, font=("Helvetica", 24))
            label.grid(row=i, column=j)
            row.append(label)
        puzzle_grid.append(row)

    prev_button = tk.Button(root, text="Prev", command=prev_state)
    next_button = tk.Button(root, text="Next", command=next_state)
    prev_button.grid(row=4, column=0)
    next_button.grid(row=4, column=2)

    root.mainloop()
