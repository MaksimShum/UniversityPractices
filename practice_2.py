import numpy as np


def solveGauss(inMatrix, inVector, dimension=3):
    """
    Solves the system of linear equations by Gauss method

    inMatrix: list (2D) of augmented matrix of a
    inMatrix = [[],[],[]]
    inVector: list of augmented matrix of b
    dimension – integer, rank of matrix representing the system.3 by default
    return: list of the solution of the system
    """

    # linear_system = inMatrix[:]
    # for i in range(dimension):
    #    linear_system[i].append(inVector[i])

    # Creating a general matrix with equations
    for i in range(dimension):
        inMatrix[i].append(inVector[i])

    # Obtaining a system of triangular equations
    for i in range(dimension):
        inMatrix[i] = list(np.divide(inMatrix[i], inMatrix[i][0]))
        for a in range(i+1, dimension):
            inMatrix[a] = list(np.subtract(inMatrix[a], np.dot(inMatrix[i], inMatrix[a][0]))[1:])

    # Searching for variables
    variables = [inMatrix[dimension-1][1]/inMatrix[dimension-1][0]]
    def variable_search(x, y, z):
        if y == z:
            return inMatrix[x][y]
        return -inMatrix[x][y]*variables[y-1] + variable_search(x, y+1, z)

    for i in range(0, dimension-1)[::-1]:
        variables.insert(0, variable_search(i, 1, dimension-i))

    return variables


# TEST BLOCK
inMatrix = [[2.50, 0.94, 0.36], [0.87, 2.30, 0.76], [0.26, 0.97, 2.15]]
inVector = [6.804, 8.415, 8.877]
print(solveGauss(inMatrix, inVector, 3))
# [1.5000, 2.1000, 3.0000]

inMatrix = [[3.9, 1.25, -0.98], [0.74, 3.45, -0.84], [-0.65, 1.18, 2.38]]
inVector = [4.905, 6.031, 10.134]
print(solveGauss(inMatrix, inVector, 3))
# Answer: x1=1.4, x2=2.3,  x3=3.5

inMatrix = [[2.5, -0.91, -0.32], [-0.91, 3.64, -0.48], [0.48, -0.98, 2.14]]
inVector = [0.287, 5.418, 5.908]
print(solveGauss(inMatrix, inVector, 3))
# Answer: x1=1.4, x2=2.3,  x3=3.5

# Practice 3
# Var 3_3
inMatrix = [[20515, 4425, 225], [4425, 979, 55], [225, 55, 5]]
inVector = [3055.3, 698.9, 56]
print(solveGauss(inMatrix, inVector, 3))

# Var 3_4
inMatrix = [[20515, 4425, 225], [4425, 979, 55], [225, 55, 5]]
inVector = [9064.6, 2011.6, 114.9]
print(solveGauss(inMatrix, inVector, 3))

# LSM Linear system of two equation
inMatrix = [[55, 15], [15, 5]]
inVector = [169.9, 46]
print(solveGauss(inMatrix, inVector, 2))
# answer = [3.19, -0.37]

# LSM Linear system of four equation
inMatrix = [[3, 1, -2, -22], [2, -1, 2, 2], [2, 1, -1, -1], [1, 1, -3, 2]]
inVector = [-2, 2, -1, -3]
print(solveGauss(inMatrix, inVector, 4))
# answer = [0, 0, 1, 0]

# Var 4_3
inMatrix = [[2.248, 0.106], [0.106, 3.047]]
inVector = [-11.5, -14.988]
print(solveGauss(inMatrix, inVector, 2))

# Var 4_4
inMatrix = [[2.248, 0.106], [0.106, 3.047]]
inVector = [-36.14, -60.611]
print(solveGauss(inMatrix, inVector, 2))
print(inMatrix)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[:]
c = [11, 12, 13, 14, 15, 16, 17]
b.append(c)
print(b)
print(a)