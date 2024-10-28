import time
from queue import LifoQueue
from functions import *

GOAL = 12345678

def DFS(state) :
    '''
    Input: 
        state : the initial state in number representation
    Output: 
        visited_size : the number of expanded nodes
        depth : the depth at which the goal state was found
        running_time : the running time of the algorithm in ms
        goal_reached : a boolean indicating whether the goal state was reached or not
        parent : a dictionary mapping each state to its parent in the search tree
    '''
    start_time = time.time()

    frontier = LifoQueue()
    frontierSet = set()
    visited = set()
    parent = {state: -1}
    goal_reached = False

    frontier.put(state)
    frontierSet.add(state)

    while not frontier.empty():
        s = frontier.get()
        frontierSet.remove(s)
        visited.add(s)

        if (s==GOAL):
            goal_reached = True
            break
        
        children = translation(s)
        for child in children:
            if (child not in visited and child not in frontierSet):
                frontier.put(child)
                frontierSet.add(child)
                parent[child] = s
    
    visited_size = len(visited)
    depth = goal_cost(parent)

    end_time = time.time()
    running_time = int((end_time - start_time) * 1000)

    return visited_size, depth, running_time, goal_reached, parent
