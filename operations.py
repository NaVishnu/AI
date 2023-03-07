import pandas as pd
import matplotlib.pyplot as plt

def union(A, B):
    C = {}
    for i in A:
        if i not in B: B[i] = 0
    for i in B: 
        if i not in A: A[i] = 0
    for i in A:
        C[i] = max(A[i], B[i])
    return C

def intersection(A, B):
    C = {}
    for i in A: 
        if i not in B: B[i] = 0
    for i in B: 
        if i not in A: A[i] = 0
    for i in A:
        C[i] = min(A[i], B[i])
    return C

def complement(A):
    C = {}
    for i in A:
        C[i] = round(1 - A[i], 1) 
    return C

def difference(A, B):
    C = {}
    for i in A: 
        if i not in B: B[i] = 0
    for i in B: 
        if i not in A: A[i] = 0
    for i in A:
        C[i] = min(A[i], round(1 - B[i], 1))
    return C

def cartesianProduct(A, B):
    return [[min(A[i], B[j]) for j in B] for i in A]

def maxMinComposition(A, B):
    C = [[0] * len(B[0])] * len(A)
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] = max(C[i][j], min(A[i][k], B[k][j]))
               
    return C

A = {2: 1, 3: 0.4, 1: 0.6, 4: 0.2}
B = {2: 0, 3: 0.2, 1: 0.2, 4: 0.8}

print('Union:', union(A, B))
print('Intersection:', intersection(A, B))
print('Complement(A):', complement(A))
print('Complement(B):', complement(B))
print('Difference:', difference(A, B))

print('De Morgan\'s Law: ', end = '')
print(complement(union(A, B)), end = ' ')
print(intersection(complement(A), complement(B)))
print(complement(union(A, B)) == intersection(complement(A), complement(B)))

A = {2: 1, 3: 0.4, 1: 0.6, 4: 0.2}
B = {5: 0, 7: 0.2, 6: 0.2, 8: 0.8}
C = {2: 0.5, 3: 0.6, 1: 0.1, 4: 0.9}

print('R = A x B')
R = cartesianProduct(A, B)
for i in R:
    print(i)

print('\nS = A x C')
S = cartesianProduct(A, C)
for i in S:
    print(i)