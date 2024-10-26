import sys
import time
from queue import Queue
from Functions import *


def solve_bfs(initial_state):
    start_time = time.time()
    goal_state = 12345678

    frontier = Queue()
    added = set([])
    visited = set([])
    parent = {initial_state: -1}

    frontier.put(initial_state)
    added.add(initial_state)
    goal_reached = False
    last1 = initial_state
    last2 = initial_state
    depth = 0

    while not frontier.empty():
        state = frontier.get()
        visited.add(state)
        if state == goal_state:
            goal_reached = True
            break
        children = translation(state)
        for child in children:
            if child not in added and child not in visited:
                last2 = child
                frontier.put(child)
                added.add(child)
                parent[child] = state
        if state == last1:
            depth += 1
            last1 = last2

    if not goal_reached:
        print("ERROR 404")
        sys.exit()

    end_time = time.time()

    print("The path to the goal")
    child_map = goal_path(parent)

    print(f"The cost of the path = {goal_cost(parent)}")

    print(f"The number of nodes expanded = {len(visited)}")

    print(f"The search depth = {depth}")

    print(f"The running time = {int((end_time - start_time) * 1000)} milliseconds")

    return parent, child_map
