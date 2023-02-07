import copy
def breadthFirstSearch(state):
    Q=[]
    Q.append(state)
    visited=[]
    visited.append(state)
    while(len(Q)>0):
        state=Q[0]
        Q.pop(0)
        print(state)
        if(state[0]==2):
            print("Goal Reached : 2 in 4")
            break
        #case1:
        state1=copy.deepcopy(state)
        state1[0]=4
        if(state1 not in visited):
            Q.append(state1)
            visited.append(state1)
            #print("Case1 : ",state1)
        #case2
        state1=copy.deepcopy(state)
        state1[1]=3
        if(state1 not in visited):
            Q.append(state1)
            visited.append(state1)
            #print("Case2 : ",state1)
        #case3
        state1=copy.deepcopy(state)
        state1[0]=0
        if(state1 not in visited):
            Q.append(state1)
            visited.append(state1)
            #print("Case3 : ",state1)
        #case4
        state1=copy.deepcopy(state)
        state1[1]=0
        if(state1 not in visited):
            Q.append(state1)
            visited.append(state1)
            #print("Case4 : ",state1)
        #case5
        state1=copy.deepcopy(state)
        if((state1[0]+state1[1])>4):
            state1[0]=4
            state1[1]=state[1]-(4-state1[0])
        else:
            state1[0]=state1[0]+state1[1]
            state1[1]=0
        if(state1 not in visited):
            Q.append(state1)
            visited.append(state1)
            #print("Case5 : ",state1)
        #case6
        state1=copy.deepcopy(state)
        if((state1[0]+state1[1])>3):
            state1[0]=state1[0]-(3-state1[1])
            state1[1]=3
        else:
            state1[1]=state1[0]+state1[1]
            state1[0]=0
        if(state1 not in visited):
            Q.append(state1)
            visited.append(state1)
            #print("Case6 : ",state1)
        print("Queue : ",Q)
        #print(visited)
 
 
state=[0,0]
breadthFirstSearch(state)
