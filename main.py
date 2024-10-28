from A_Star import solve_a_start
from BFS import *
import tkinter as tk


def update_puzzle():
    global state, puzzle_grid
    state_list = number_to_state(state)
    for i in range(3):
        for j in range(3):
            if not state_list[i][j] == "0":
                puzzle_grid[i][j].config(text=state_list[i][j], bg="grey", fg="white",
                                         width=8, height=4, bd=4, relief="solid",
                                         highlightbackground="black", highlightthickness=3, font=("Helvetica", 24))
            else:
                puzzle_grid[i][j].config(text=state_list[i][j], bg="black", fg="black",
                                         width=8, height=4, bd=4, relief="flat",
                                         highlightbackground="black", highlightthickness=3, font=("Helvetica", 24))


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


def gui():
    global initial_state, puzzle_grid
    root = tk.Tk()
    root.title("8-Puzzle Game")

    window_width = 380
    window_height = 450
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_x = (screen_width // 2) - (window_width // 2)
    position_y = (screen_height // 2) - (window_height // 2)
    root.geometry(f'{window_width}x{window_height}+{position_x}+{position_y}')

    initial_state = number_to_state(initial_state)
    for i in range(3):
        row = []
        for j in range(3):
            if not initial_state[i][j] == "0":
                label = tk.Label(root, text=initial_state[i][j], bg="grey",
                                 width=8, height=4, bd=4, relief="solid",
                                 highlightbackground="black", highlightthickness=3, font=("Helvetica", 24))
            else:
                label = tk.Label(root, text=initial_state[i][j], fg="black", bg="black", width=8, height=4,
                                 bd=4, highlightbackground="black", highlightthickness=3, font=("Helvetica", 24))
            label.grid(row=i, column=j)
            row.append(label)
        puzzle_grid.append(row)

    prev_button = tk.Button(root, text="<--", width=6, height=2,
                            bd=3, font=("Helvetica", 24), command=prev_state)
    next_button = tk.Button(root, text="-->", width=6, height=2,
                            bd=3, font=("Helvetica", 24), command=next_state)
    prev_button.grid(row=4, column=0)
    next_button.grid(row=4, column=2)

    root.mainloop()


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
                expanded, depth, time, parent = solve_bfs(initial_state)
            case "2":
                print("DFS")
            case "3":
                print("iterative DFS")
            case "4":
                expanded, depth, time, parent = solve_a_start(initial_state, 1)
            case "5":
                expanded, depth, time, parent = solve_a_start(initial_state, 0)
            case _:
                choice = False

    print("The path to the goal")
    child = goal_path(parent)

    print(f"The cost of the path = {goal_cost(parent)}")

    print(f"The number of nodes expanded = {expanded}")

    print(f"The search depth = {depth}")

    print(f"The running time = {time} milliseconds")

    state = initial_state
    puzzle_grid = []
    gui()



