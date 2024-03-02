import numpy as np


def modelMatrix(inMatrix, sequence):
    """
    Finds a transformation vector in 2D.

    inMatrix: dictionary of transformation matrix
    inMatrix = {'R':(angle),'T':( T_x, T_y),'S':( S_x, S_y),'V':(x,y)}
    sequence – string of operation, like 'TRS', T – first, S - last
    returns: tuple of transformed vector
    """

    result_matrix = [float(i) for i in inMatrix["V"]]
    result_matrix.append(1.0)

    for operation in sequence[::-1]:
        if operation == 'S':
            result_matrix = np.dot([[inMatrix['S'][0], 0.0, 0.0], [0.0, inMatrix['S'][1], 0.0], [0.0, 0.0, 1.0]], result_matrix)
        elif operation == 'T':
            result_matrix = np.dot([[1.0, 0.0, inMatrix['T'][0]], [0.0, 1.0, inMatrix['T'][1]], [0.0, 0.0, 1.0]], result_matrix)
        else:
            result_matrix = np.dot([[np.cos(inMatrix['R']*(np.pi/180)), -(np.sin(inMatrix['R']*(np.pi/180))), 0.0], [np.sin(inMatrix['R']*(np.pi/180)), np.cos(inMatrix['R']*(np.pi/180)), 0.0], [0.0, 0.0, 1.0]], result_matrix)

    return result_matrix


#TEST BLOCK
inMatrix = {'R': 33.0, 'T': (1.0, 2.0), 'S': (2.0, 1.2), 'V': (1.0,2.0)}
print(modelMatrix(inMatrix, 'SRT'))
#(-1.0, 5.33, 1)

inMatrix = {'R':(16),'T':(1.0,2.0),'S':(1.0,2.0),'V':(1.0,2.0)}
print(modelMatrix(inMatrix, 'TRS'))
#(0.86, 6.12, 1)


print("\nVar_1_j")
inMatrix = {'R': (51.2), 'T': (1.0, 2.0), 'S': (3.0, 1.2), 'V': (1, 4)}
print(modelMatrix(inMatrix, 'RST'))

print("\nVar_1_k")
inMatrix = {'R': 10, 'T': (1.0, 2.0), 'S': (1.0, 1.2), 'V': (1, 4)}
print(modelMatrix(inMatrix, 'TRS'))


print("\nVar_3_j")
inMatrix = {'R': 15, 'T': (2.0, 2.0), 'S': (1.5, 2.7), 'V': (6, 2)}
print(modelMatrix(inMatrix, 'SRT'))

print("\nVar_3_k")
inMatrix = {'R':(51.0),'T':(3.0,2.0),'S':(1.0,3.2),'V':(6,2)}
print(modelMatrix(inMatrix, 'TRS'))

