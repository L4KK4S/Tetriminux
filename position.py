def emplace_bloc(grid,bloc,i ,j):
    """
                Place the bloc at position (i,j)
                :param: grid, bloc,i,j
                :type : list, list,int,int
                :return: grid
                :rtype: list
                :Example:
                     >>> emplace_bloc([[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,0,0,1]],[[0,0,0],[0,2,2]],2,1)
                        grid:
                        [[1,0,0,1],[1,0,0,1],[1,2,2,1],[1,0,0,1]]
                    """
    for x in range(len(bloc)):
        for y in range(len(bloc[x])):
            if bloc[x][y] == 2:
                grid[i-len(bloc)+1+x][j+y]=2
    return grid

def valid_position(grid, bloc,i,j):
    """
                Determined if the block can be in the position (i,j)
                :param: grid, bloc,i,j
                :type : list, list,int,int
                :return: valid
                :rtype: bool
                :Example:
                     >>> valid_position([[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,0,0,1]],[[0,0,0],[0,2,2]],2,1)
                        True
                        """
    for x in range(len(bloc)):
        for y in range(len(bloc[x])):
            if ((i - x) >= len(grid) or j + y >= len(grid[x]) or (i - x) < 0):
                if bloc[4 - x][y] == 2:
                    return False
            elif bloc[4 - x][y] == 2:
                if grid[i - x][j + y] == 2 or grid[i - x][j + y] == 1:
                    return False
    return True



def choix_position(alphabet, alphabet2=None):
    """
                Request to the player the coordinates (i,j)
                :param: alphabet
                :type : str
                :return: i,j
                :rtype: int,int
                :Example:
                     >>> choix_position(alphabet)
                        (4,7)
                        """
    if alphabet2 is None:
        i=input("Choisissez la ligne\n>>> ").lower()
        while i not in alphabet:
            print("Vous ne pouvez pas positionnez cette pièce ici")
            i=(input(">>> ")).lower()
        j = input("Choisissez la colonne\n>>> ").lower()
        while j not in alphabet:
            print("Vous ne pouvez pas positionnez cette pièce ici")
            j = input(">>> ").lower()
        return i,j
    else:
        i = input("Choisissez la ligne\n>>> ").lower()
        while i not in alphabet:
            print("Vous ne pouvez pas positionnez cette pièce ici")
            i = (input(">>> ")).lower()
        j = input("Choisissez la colonne\n>>> ").lower()
        while j not in alphabet2:
            print("Vous ne pouvez pas positionnez cette pièce ici")
            j = input(">>> ").lower()
        return i, j


