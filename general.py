#1) DFS
graph = [[1, 2], [2, 4], [1, 4], [3, 4], [3, 5], [2, 6], [3, 6], [4, 5], [5, 6]]
start = 1
end = 6
stack = [start]
path = [start]

while stack[-1]!=end:
    temp = stack[-1]
    del stack[-1]
    count = 0
    for edge in graph:
        if edge[0]==temp:
            path.append(edge[1])
            stack.append(edge[1])
            count += 1
    if count==0:
        del path[-1]
        
print(path)

#2) Recursive DFS:
graph = [[1, 2], [2, 4], [1, 4], [3, 4], [3, 5], [2, 6], [3, 6], [4, 5], [5, 6]]
start = 1
end = 6
path = [start]

while start!=end:
    for edge in graph:
        if edge[0]==start:
            start = edge[1]
            break
    path.append(start)
  
print(path)

#3) BFS
graph = [[1, 2], [2, 4], [1, 4], [3, 4], [3, 5], [2, 6], [3, 6], [4, 5], [5, 6]]
start = 1
end = 6
queue = []
queue.append([start])

while(len(queue)>0):
    path = queue.pop(0)
    node = path[-1]
    
    if node==end:
        print(path)
        break

    for edge in graph:
        if edge[0]==node:
            new_path = list(path)
            new_path.append(edge[1])
            queue.append(new_path)

#4) Depth Limited Search
def dls(graph, start, end, depth):
    stack = [[start, 0, -1]]
    path = [[start, 0, -1]]
    while len(stack)>0 and stack[-1][0]!=end:
        node = stack[-1]
        del stack[-1]
        if node[1]>=depth:
            continue
        
        for edge in graph:
            if edge[0]==node[0]:
                stack.append([edge[1], node[1]+1, node[0]])
                path.append([edge[1], node[1]+1, node[0]])
        
    if path[-1][0]==end:
        route = []
        route.append(path[-1][0])
        route.append(path[-1][2])
        del path[-1]
        path.reverse()
        for node in path:
            if node[0]==route[-1] and route[-1]!=-1:
                route.append(node[2])
        del route[-1]
        route.reverse()
        print(route)

#5) Iterative Deepening DFS:
graph = [[1, 2], [2, 4], [1, 4], [3, 4], [3, 5], [2, 6], [3, 6], [4, 5], [5, 6]]
start = 1
end = 6
limit = 3
            
def dls(graph, start, end, depth):
    stack = [[start, 0, -1]]
    path = [[start, 0, -1]]
    while len(stack)>0 and stack[-1][0]!=end:
        node = stack[-1]
        del stack[-1]
        if node[1]>=depth:
            continue
        
        for edge in graph:
            if edge[0]==node[0]:
                stack.append([edge[1], node[1]+1, edge[0]])
                path.append([edge[1], node[1]+1, edge[0]])
    print("Depth: ", depth, "Path: ", path)
    if path[-1][0]==end:
        route = []
        route.append(path[-1][0])
        route.append(path[-1][2])
        del path[-1]
        path.reverse()
        for edge in path:
            if edge[0]==route[-1] and route[-1]!=-1:
                route.append(edge[2])
        del route[-1]
        route.reverse()
        return [True, route]
    else:
        return [False, []]
            
def iddfs(graph, start, end, limit):
    for i in range(1, limit+1):
        res = dls(graph, start, end, i)
        if res[0]:
            break
    print(res[1])
        
iddfs(graph, start, end, limit)

#6) A* algorithm (Genral)
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            is_closed = False
            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    is_closed = True
            if is_closed:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

start = (0, 0)
end = (9, 9)

path = astar(maze, start, end)
print(path)

#7) 8 puzzle problem using A*
def displaced_tiles(state):
    if state[1] == 0:
        return 0

    heuristic = 0

    for i in range(len(state)):
        if state[0][i] != i:
            heuristic += 1

    return state[1] + heuristic

def manhattan_distance(state):
    if state[1] == 0:
        return 0

    heuristic = 0
    k = 0

    for i in range(3):
        for j in range(3):
            heuristic += abs(i - (state[0][k] / 3)) + abs(j - (state[0][k] % 3))
            k += 1

    return state[1] + heuristic

def getNextState(state):
    nextStates = []
    pos0 = state[0].index(0)

    for i in adjacency[pos0]:
        nextState = [x for x in state[0]]
        temp = nextState[i]
        nextState[i] = 0
        nextState[pos0] = temp
        nextStates.append([nextState, state[1] + 1])

    return nextStates

def listEqual(l1, l2):
    if len(l1) != len(l2):
        return False
    
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False

    return True

def aStar(start, end, sortFun):
    queue = [[start, 0]]
    visited = []

    while len(queue) > 0:
        queue = sorted(queue, key = sortFun)

        print("Queue:", queue)
        print("Visited Nodes:", visited)
        print()

        n = queue[0]
        del queue[0]
        visited.append(n[0])
        
        nextStates = getNextState(n)
        for state in nextStates:
            if listEqual(state[0], end):
                print("End State:", state[0])
                print("Number of states visited:", len(visited))
                return True

            if state[0] not in visited:
                queue.append(state)
    
    return False

# start = [7, 2, 4, 5, 0, 6, 8, 3, 1]
# start = [1, 4, 2, 3, 0, 5, 6, 7, 8]
start = [1, 0, 4, 3, 5, 2, 6, 7, 8]
end = [0, 1, 2, 3, 4, 5, 6, 7, 8]

adjacency = {
             0: [1, 3], 
             1: [0, 2, 4], 
             2: [1, 5], 
             3: [0, 4, 6], 
             4: [1, 3, 5, 7], 
             5: [2, 4, 6], 
             6: [5, 7], 
             7: [4, 6, 8], 
             8: [5, 7]
            }

print("Manhattan Distance:")
if aStar(start, end, manhattan_distance):
    print("Solution found!\n\n")
else:
    print("No Solution!\n\n")

print("Displaced Tiles:")
if aStar(start, end, displaced_tiles):
    print("Solution found!")
else:
    print("No Solution!")

#8) 8-puzzle using hill climbing
def displaced_tiles(state):
    heuristic = 0

    for i in range(len(state)):
        if state[i] != i:
            heuristic += 1

    return heuristic

def manhattan_distance(state):
    heuristic = 0
    k = 0

    for i in range(3):
        for j in range(3):
            heuristic += abs(i - (state[k] / 3)) + abs(j - (state[k] % 3))
            k += 1

    return heuristic

def getNextState(state):
    nextStates = []
    pos0 = state.index(0)

    for i in adjacency[pos0]:
        nextState = [x for x in state]
        temp = nextState[i]
        nextState[i] = 0
        nextState[pos0] = temp
        nextStates.append(nextState)

    return nextStates

def listEqual(l1, l2):
    if len(l1) != len(l2):
        return False
    
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False

    return True

def hill_climb(start, end, sortFun):
    queue = [start]
    visited = []

    while len(queue) > 0:
        queue = sorted(queue, key = sortFun)
        # Displaced Tiles - 1122
        # Manhattan Distance - 2611

        # print("Queue:", queue)
        # print("Visited Nodes:", visited)
        # print()

        n = queue[0]
        del queue[0]

        if listEqual(n, end):
            print("End State:", n)
            print("Number of states visited:", len(visited))
            return True
        
        nextStates = getNextState(n)
        for state in nextStates:
            # if state not in visited and sortFun(state) < sortFun(n):
            if state not in visited:
                queue.append(state)
        visited.append(n)
    
    return False

start = [7, 2, 4, 5, 0, 6, 8, 3, 1]
# start = [1, 4, 2, 3, 0, 5, 6, 7, 8]
# start = [1, 0, 2, 3, 4, 5, 6, 7, 8]
# start = [0, 1, 2, 3, 4, 5, 6, 7, 8]
end = [0, 1, 2, 3, 4, 5, 6, 7, 8]

adjacency = {
             0: [1, 3], 
             1: [0, 2, 4], 
             2: [1, 5], 
             3: [0, 4, 6], 
             4: [1, 3, 5, 7], 
             5: [2, 4, 6], 
             6: [5, 7], 
             7: [4, 6, 8], 
             8: [5, 7]
            }

print("Manhattan Distance:")
if hill_climb(start, end, manhattan_distance):
    print("Solution found!\n\n")
else:
    print("No Solution!\n\n")

print("Displaced Tiles:")
if hill_climb(start, end, displaced_tiles):
    print("Solution found!")
else:
    print("No Solution!")
    

#9) Missionaries and Cannibal
from copy import copy, deepcopy

def leftBankCount(state):
    return state[0][0] + state[0][1]

def isSafe(state):
    if (state[0][1] > 0 and state[0][0] > state[0][1]) or (state[1][1] > 0 and state[1][0] > state[1][1]):
        return False
    else:
        return True

def getNextState(state):
    nextStates = []
    
    if state[2] == 0:
        temp = deepcopy(state)
        if temp[0][0] >= 2:
            temp[0][0] -= 2 
            temp[1][0] += 2
            if isSafe(temp):
                temp[2] = 1
                nextStates.append(temp)
        temp = deepcopy(state)
        if temp[0][1] >= 2:
            temp[0][1] -= 2
            temp[1][1] += 2
            if isSafe(temp):
                temp[2] = 1
                nextStates.append(temp)
        temp = deepcopy(state)
        if temp[0][0] >= 1 and temp[0][1] >= 1:
            temp[0][0] -= 1
            temp[0][1] -= 1
            temp[1][0] += 1
            temp[1][1] += 1
            if isSafe(temp):
                temp[2] = 1
                nextStates.append(temp)
        temp = deepcopy(state)
        if temp[0][0] >= 1:
            temp[0][0] -= 1
            temp[1][0] += 1
            if isSafe(temp):
                temp[2] = 1
                nextStates.append(temp)
        temp = deepcopy(state)
        if temp[0][1] >= 1:
            temp[0][1] -= 1
            temp[1][1] += 1
            if isSafe(temp):
                temp[2] = 1
                nextStates.append(temp)
    else:
        temp = deepcopy(state)
        if temp[1][0] >= 2:
            temp[1][0] -= 2 
            temp[0][0] += 2
            if isSafe(temp):
                temp[2] = 0
                nextStates.append(temp)
        temp = deepcopy(state)
        if temp[1][1] >= 2:
            temp[1][1] -= 2
            temp[0][1] += 2
            if isSafe(temp):
                temp[2] = 0
                nextStates.append(temp)
        temp = deepcopy(state)
        if temp[1][0] >= 1 and temp[1][1] >= 1:
            temp[1][0] -= 1
            temp[1][1] -= 1
            temp[0][0] += 1
            temp[0][1] += 1
            if isSafe(temp):
                temp[2] = 0
                nextStates.append(temp)
        temp = deepcopy(state)
        if temp[1][0] >= 1:
            temp[1][0] -= 1
            temp[0][0] += 1
            if isSafe(temp):
                temp[2] = 0
                nextStates.append(temp)
        temp = deepcopy(state)
        if temp[1][1] >= 1:
            temp[1][1] -= 1
            temp[0][1] += 1
            if isSafe(temp):
                temp[2] = 0
                nextStates.append(temp)

    # print("Next States:", nextStates)
    return nextStates

def listEqual(l1, l2):
    if l1[0][0] == l2[0][0] and l1[0][1] == l2[0][1] and l1[1][0] == l2[1][0] and l1[1][1] == l2[1][1] and l1[2] == l2[2]:
        return True
    else:
        return False

def hill_climb(start, end):
    queue = [start]
    visited = []

    while len(queue) > 0:
        queue = sorted(queue, key = leftBankCount)

        print("Queue:", queue)
        # print("Visited Nodes:", visited)
        # print()

        n = queue[0]
        del queue[0]

        if listEqual(n, end):
            print("End State:", n)
            print("Number of states visited:", len(visited))
            return True
        
        nextStates = getNextState(n)
        for state in nextStates:
            # if state not in visited and sortFun(state) < sortFun(n):
            if state not in visited:
                queue.append(state)
        visited.append(n)
    
    return False

start = [[3, 3], [0, 0], 0]
# start = [[2, 0], [1, 3], 1]
end = [[0, 0], [3, 3], 1]

if hill_climb(start, end):
    print("Solution found!\n\n")
else:
    print("No Solution!\n\n")
