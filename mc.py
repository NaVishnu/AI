#5) Missionaries and Cannibals
def isValid2(state):
    if state[0]<0 or state[1]<0 or state[2]<0 or state[0]>3 or state[1]>3 or state[2]>1 or (0<state[0]<state[1]) or (0<(3-state[0])<(3-state[1])):
        return False
    else:
        return True

def generateStates(M, C, B):
    moves = [[1, 0, 1], [0, 1, 1], [2, 0, 1], [0, 2, 1], [1, 1, 1]]
    children = []
    for each in moves:
        if B==1:
            nextState = [x1-x2 for (x1, x2) in zip([M, C, B], each)]
        else:
            nextState = [x1+x2 for (x1, x2) in zip([M, C, B], each)]
        if isValid2(nextState):
            children.append(nextState)
    return children
    
solution = []
def solution2(M, C, B, visited):
    if ([M, C, B]==[0, 0, 0]):
        solution.append(visited+[[0, 0, 0,]])
        return True
    elif ([M, C, B] in visited):
        return False
    else:
        visited.append([M, C, B])
        if B==1:
            for each in generateStates(M, C, B):
                solution2(each[0], each[1], each[2], visited)
        else:
            for each in generateStates(M, C, B):
                solution2(each[0], each[1], each[2], visited)
             
solution2(3, 3, 1, [])
solution.sort()
for each in solution:
    print(each)
