import math


def enter_state(state):
    print("Enter the initial state of 8 puzzle:")
    num = 0
    try:
        for i in range(3):
            row = list(map(int, input().split()))
            if not len(row) == 3:
                return False
            for j in row:
                if j < 0 or j > 8:
                    return False
                num += pow(10, j)
            state.append(row)
        if not num == 111111111:
            return False
        return True
    except Exception as e:
        return False


def print_state(state):
    print("-----------------------------------")
    for row in state:
        print(list(map(int, row)))


def solvable(state):
    state_str = str(state)
    inversions = 0
    for i in range(len(state_str)):
        if state_str[i] == '0':
            continue
        for j in range(i + 1, len(state_str)):
            if state_str[j] == '0':
                continue
            if state_str[j] < state_str[i]:
                inversions = inversions + 1
    return inversions % 2 == 0


def state_to_number(state):
    num = 0
    for row in range(3):
        for col in range(3):
            num += pow(10, 8 - 3 * row - col) * state[row][col]
    return num


def number_to_state(num):
    num_str = str(num)
    if len(num_str) == 8: num_str = '0' + num_str
    state = []
    row = []
    for i in range(9):
        row.append(num_str[i])
        if i % 3 == 2:
            state.append(row)
            row = []
    return state


def test(state):
    print_state(state)
    print(state_to_number(state))
    print(number_to_state(state_to_number(state)))
    list = translation(state_to_number(state))
    print(list)


def swap(string, i, j):
    string_list = list(string)
    string_list[i], string_list[j] = string_list[j], string_list[i]
    return ''.join(string_list)


def translation(state):
    state_str = str(state)
    if len(state_str) == 8:
        state_str = '0' + state_str
    zero_pos = 0
    children = []
    for i in range(9):
        if state_str[i] == '0':
            zero_pos = i
            break
    if zero_pos > 2:
        children.append(int(swap(state_str, zero_pos, zero_pos - 3)))
    if zero_pos % 3 != 0:
        children.append(int(swap(state_str, zero_pos, zero_pos - 1)))
    if zero_pos % 3 != 2:
        children.append(int(swap(state_str, zero_pos, zero_pos + 1)))
    if zero_pos < 6:
        children.append(int(swap(state_str, zero_pos, zero_pos + 3)))
    return children


def goal_path(parent):
    path = []
    state = 12345678
    child = {12345678: -1}
    while not parent[state] == -1:
        path.append(state)
        child[parent[state]] = state
        state = parent[state]
    path.append(state)
    path.reverse()
    for state1 in path:
        print_state(number_to_state(state1))
    print("-----------------END------------------")
    return child


def goal_cost(parent):
    state = 12345678
    cost = 0
    while not parent[state] == -1:
        state = parent[state]
        cost += 1
    return cost


def decreaseKey(frontier, child, curr_cost):
    for cost, state in frontier:
        if state == child and cost > curr_cost:
            cost = curr_cost
            break
    return


def manhattan_distance(state, original_cell_pos):
    distance = 0
    state_str = str(state)
    for i in range(len(state_str)):
        if state_str[i] != '0':
            target_row, target_col = original_cell_pos[int(state_str[i])]
            current_row, current_col = i / 3, i % 3
            distance += abs(target_row - current_row) + abs(target_col - current_col)
    return distance


def euclidean_distance(state, original_cell_pos):
    distance = 0
    state_str = str(state)
    for i in range(len(state_str)):
        if state_str[i] != '0':
            target_row, target_col = original_cell_pos[int(state_str[i])]
            current_row, current_col = i / 3, i % 3
            distance += math.sqrt((target_row - current_row) ** 2 + (target_col - current_col) ** 2)
    return distance

