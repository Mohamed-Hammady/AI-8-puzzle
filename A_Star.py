import sys
import time
import heapq  
from Functions import *
# 0 for euclidean and 1 for manhatten
def a_star(initial_state, method_Flag):
    start_time = time.time()
    goal_state = 12345678
    frontier = []
    currently_in_frontier=set([])
    visited = set([])
    cost_so_far = {initial_state: 0}
    parent = {initial_state: -1}
    original_cell_pos = {
        0: (0, 0), 1: (0, 1), 2: (0, 2),
        3: (1, 0), 4: (1, 1), 5: (1, 2),
        6: (2, 0), 7: (2, 1), 8: (2, 2)
    }
    heapq.heappush(frontier, (0,initial_state))
    currently_in_frontier.add(initial_state)
    goal_reached = False
    
    while not len(frontier) == 0:
        current_total_cost, curr_state = heapq.heappop(frontier)
        currently_in_frontier.remove(curr_state)
        visited.add(curr_state)
        
        if curr_state == goal_state:
            depth = cost_so_far[curr_state]
            goal_reached = True
            break
        
        curr_cost = cost_so_far[curr_state]
        
        children = translation(curr_state)
        for child in children:
            
            new_cost = curr_cost + 1
            
            if child not in currently_in_frontier and child not in visited: 
                if method_Flag:
                    heuristic = manhattan_distance(child, original_cell_pos)
                else:
                    heuristic = euclidean_distance(child, original_cell_pos)
                
                priority = new_cost + heuristic 
                heapq.heappush(frontier, (priority, child))
                currently_in_frontier.add(child)
                
                cost_so_far[child] = new_cost 
                parent[child] = curr_state
                
            elif child in currently_in_frontier:
                if method_Flag:
                    heuristic = manhattan_distance(child, original_cell_pos)
                else:
                    heuristic = euclidean_distance(child, original_cell_pos)
                curr_cost = heuristic + cost_so_far[child]
                decreaseKey(frontier, child, curr_cost)

    end_time = time.time()
    running_time=int((end_time - start_time) * 1000)
    return parent, visited, depth, running_time, goal_reached