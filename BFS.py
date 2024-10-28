import time
from queue import Queue
from Functions import *


def solve_bfs(initial_state):
    start_time = time.time()
    goal_state = 12345678

    frontier = Queue()
    added = set([])  # states added to the frontier
    visited = set([])
    parent = {initial_state: -1}

    frontier.put(initial_state)
    added.add(initial_state)
    goal_reached = False

    while not frontier.empty():
        state = frontier.get()
        visited.add(state)
        if state == goal_state:
            goal_reached = True
            break
        children = translation(state)
        for child in children:
            if child not in added and child not in visited:
                frontier.put(child)
                added.add(child)
                parent[child] = state

    end_time = time.time()

    return len(visited), goal_cost(parent), int((end_time - start_time) * 1000), goal_reached, parent
