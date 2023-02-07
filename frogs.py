#1) Six Frogs and Seven Poles
start = 'abcd-uvwx'
goal = 'uvwx-abcd'
#Frogs on the right in the goal state
right = 'abcd'
#Frogs on the left in the goal state
left = 'uvwx'
 
#Function for swapping the frogs
def swap(state, i, j):
    return state[:i]+state[j]+state[i+1:j]+state[i]+state[j+1:]
 
#Function for applying the movies to generate the states
def apply(state, tbm):
    i = state.index(tbm)
    if tbm in right:
        if i+1<len(state) and state[i+1]=='-':
            return swap(state, i, i+1)
        if i+2<len(state) and state[i+1]!='-' and state[i+2]=='-':
            return swap(state, i, i+2)
    if tbm in left:
        if i-1>=0 and state[i-1]=='-':
            return swap(state, i-1, i)
        if i-2>=0 and state[i-1]!='-' and state[i-2]=='-':
            return swap(state, i-2, i)
 
#Function that returns the states that can be moved to generate the next states     
def nextMoves(state):
    i = state.index('-')
    #Possible swaps (to be moved)
    tbm = []
 
    if i-1>=0 and state[i-1] in right:
        tbm.append(state[i-1])
    if i-2>=0 and state[i-2] in right:
        tbm.append(state[i-2])
    if i+1<len(state) and state[i+1] in left:
        tbm.append(state[i+1])
    if i+2<len(state) and state[i+2] in left:
        tbm.append(state[i+2])
    return tbm
 
#Function that performs blind search
def search(start):
    work = set([("", start)])
    cont = True
    while (cont):
        path, current = work.pop()
        for k in nextMoves(current):
            suc = apply(current, k)
            work.add((path+k, suc))
            if suc==goal:
                print(path+k, " is the path")
                cont = False
                break
 
search(start)
