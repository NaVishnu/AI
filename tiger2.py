from collections import namedtuple
from enum import Enum
from functools import partial
 
def isValid(state):
    goatEat = state.goat==state.grass and state.man!=state.goat
    tigerEat = state.goat==state.tiger and state.man!=state.goat
    invalid = goatEat or tigerEat
    return not invalid
 
def nextState(state):
    if state.man==Location.A:
        otherSide = Location.B
    else:
        otherSide = Location.A
 
    move = partial(state._replace, man=otherSide)
    children = [move()]
 
    for character in ["goat", "grass", "tiger"]:
        if getattr(state, character)==state.man:
            children.append(move(** {character:otherSide}))
 
    yield from filter(isValid, children)
 
def search(start, isGoal, neighbours):
    parent = dict()
    visit = [start]
    visited = set([start])
 
    while (visit):
        vertex = visit.pop(0)
        if isGoal(vertex):
            path = []
            while vertex is not None:
                path.insert(0, vertex)
                vertex = parent.get(vertex)
            return path
        for neighbour in neighbours(vertex):
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = vertex
                visit.append(neighbour)
 
def solution(path):
    for old, new in zip(path, path[1:]):
        boat = [character for character in ['man', 'goat', 'grass', 'tiger'] if getattr(old, character)!=getattr(new, character)]
        print(old.man, ' to ', new.man, boat)
 
State = namedtuple("State", ["man", "grass", "goat", "tiger"])
Location = Enum("Location", ['A', 'B'])
start = State(man = Location.A, grass = Location.A, goat = Location.A, tiger = Location.A)
goal = State(man = Location.B, grass = Location.B, goat = Location.B, tiger = Location.B)
path = search(start=start, isGoal=goal.__eq__, neighbours=nextState)
solution(path)
