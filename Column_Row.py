def row_clear(grid,i):
    """
            Clear a row which all the row is complet and drops the blocks from above.
            :param: grid, i
            :type : list, int
            :return: grid, nb_case
            :rtype: list,int
            :Example:
                 >>> row_clear([[1,2,1],[1,2,2],[0,1,1]],1)
                  grid = [[1,0,1],[1,2,0],[0,1,1]]
    """
    nb_case=0
    for j in range(len(grid[0])):
        if grid[i][j]==2:
            grid[i][j]=0
            nb_case+=1
    for j in range(1,i+1):
        for k in range(len(grid[j])):
            if grid[-(j+len(grid)-i)+1][k]!=1 and grid[-(j+len(grid)-i)][k]!=1:
                grid[-(j+len(grid)-i)+1][k]=grid[-(j+len(grid)-i)][k]
            elif grid[-(j+len(grid)-i)+1][k]!=1 and grid[-(j+len(grid)-i)][k]==1:
                grid[-(j + len(grid) - i) + 1][k] = 0
    for j in range(len(grid[0])):
        if grid[0][j]!=1:
            grid[0][j]=0
    return grid,nb_case

def row_state(grid,i):
    """
            Determined if a row is complet
            :param: grid, i
            :type : list, int
            :return: pleine
            :rtype: bool
            :Example:
                 >>> row_state([[1,2,1],[1,2,2],[0,1,1]],1)
                    False
    """
    j = 0
    while j < len(grid[0]):
        if grid[i][j] == 0:
            return False
        j += 1
    return True

def col_clear(grid,j):
    """
            Clear a column which all the column is complet.
            :param: grid, j
            :type : list, int
            :return: grid, nb_case
            :rtype: list,int
            :Example:
                 >>> col_clear([[1,2,1],[1,2,2],[0,2,1]],1)
                  grid = [[1,0,1],[1,0,2],[0,0,1]]
    """
    nb_case=0
    for i in range(len(grid)):
        if grid[i][j]==2:
            nb_case+=1
            grid[i][j]=0
    return grid,nb_case

def col_state(grid,j):
    """
            Determined if a column is complet
            :param: grid, j
            :type : list, int
            :return: pleine
            :rtype: bool
            :Example:
                 >>> col_state([[1,2,1],[1,2,2],[0,1,1]],1)
                    True
    """
    pleine=True
    i=0
    while pleine==True and i<len(grid):
        try:
            if grid[i][j]==0:
                pleine=False
        except:
            pass
        i+=1
    return pleine
