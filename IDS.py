import time
from queue import LifoQueue
from Functions import *

GOAL = 12345678
MAX_LIMIT = 362881 # number of possible permutations of the tiles + 1

def DLS(state, limit):
    '''
    Input: 
        state : the initial state in number representation
    Output: 
        goal_reached : a boolean indicating whether the goal state was reached or not
        visited_size : the number of expanded nodes
        parent : a dictionary mapping each state to its parent in the search tree
    '''
    frontier = LifoQueue() # stores tuples of states and their depth when reached
    min_depth = {}
    parent = {state: -1}

    goal_reached = False
    frontier.put((state, 0))

    while not frontier.empty():
        s_value, s_depth = frontier.get()
        if (s_value in min_depth and min_depth[s_value]<=s_depth):
            continue

        min_depth[s_value] = s_depth
        if (s_value==GOAL):
            goal_reached = True
            break
        
        if s_depth<limit:
            children = translation(s_value)
            for child in children:
                if child!=state:
                    frontier.put((child, s_depth+1))
                    parent[child] = s_value
    
    visited_size = len(min_depth)
    return goal_reached, visited_size, parent

def IDS(state):
    '''
    Input: 
        state : the initial state in number representation
    Output: 
        visited_size : the number of expanded nodes over all the iterations
        depth : the depth at which the goal state was found
        running_time : the running time of the algorithm in ms
        goal_reached : a boolean indicating whether the goal state was reached or not
        parent : a dictionary mapping each state to its parent in the search tree
    '''
    start_time = time.time()

    goal_reached = False
    visited_size = 0

    output = None
    depth = 0
    for l in range(MAX_LIMIT):
        output = DLS(state, l)
        visited_size += output[1]
        if output[0] == True:
            goal_reached = True
            depth = l
            break
    
    end_time = time.time()
    parent = output[2]
    running_time = int((end_time - start_time) * 1000)
    return visited_size, depth, running_time, goal_reached, parent
