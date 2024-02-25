def modelMatrix(inMatrix, sequence):
    """
    Finds a transformation vector in 2D.

    inMatrix: dictionary of transformation matrix
    inMatrix = {'R':(angle),'T':( T_x, T_y),'S':( S_x, S_y),'V':(x,y)}
    sequence – string of operation, like 'TRS', T – first, S - last
    returns: tuple of transformed vector
    """
    ### TODO









#TEST BLOCK
inMatrix = {'R':(33),'T':(1.0,2.0),'S':(2.0,1.2),'V':(1,2)}
modelMatrix(inMatrix, 'SRT')
#(-1.0, 5.33, 1)
inMatrix = {'R':(16),'T':(1.0,2.0),'S':(1.0,2.0),'V':(1,2)}
modelMatrix(inMatrix, 'TRS')
#(0.86, 6.12, 1)

