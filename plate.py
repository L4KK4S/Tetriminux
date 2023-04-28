import random

def read_grid(path):
    """
            Create the grid from a txt file.

            :param: /
            :type : /
            :return: grid
            :rtype: list
            :Example:
                 >>> read_grid()
                  grid = [[1,1,1],[1,0,0],[0,1,1]]
    """
    grid=[]
    path = open(path, 'r')
    lignes = path.readlines()
    for ligne in lignes: #Lis ligne par ligne puis chaque élément par ligne pour créer notre matrice grid
        L=[]
        for elt in ligne:
            if elt!=" " and elt!="\n":
                L.append(int(elt))
        grid.append(L)
    path.close()
    return grid

def save_grid(path,grid,shape, score):
    """
            Save the grid in a txt file.

            :param grid: The grid to save
            :param path: The file txt who save grid
            :param: shape: The shape of the grid
            :type grid: list
            :type: path: str
            :type: shpae: str
            :return:
            :rtype:
            :Example:
                 >>> save_grid('saved_game.txt',[[1, 1, 1], [1, 0, 1], [1, 1, 2]], 3, 22)
                save_game.txt:
                  1 1 1
                  1 0 1
                  1 1 2
                shape.txt:
                  3
                  22
        """
    with open(path, "w") as file, open("saved_game_data.txt", "w") as second_file:
        for lignes in grid:
            for elt in lignes:
                file.write(str(elt)+" ")
            file.write("\n")
        second_file.write(f'{shape}\n{score}')
        return

def print_grid(grid):
    """
        Draw the grid in the terminal.

        :param grid: The grid to draw
        :type grid: list
        :return: /
        :rtype: /
        :Example:
             >>> print_grid([[1, 1, 1], [1, 0, 1], [1, 1, 2]])
               A B C
              ╔══════╗
            a ║      ║
            b ║  ◦   ║
            c ║    ■ ║
              ╚══════╝
    """
    alphabet_maj = " A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    alphabet_min = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    grid_drawed = "    " + alphabet_maj[0:len(grid[0] * 2)] + "\n   ╔" + "══" * len(grid[0]) + "═╗"
    for i, row in enumerate(grid):
        temp_line = f"{alphabet_min[(i * 2)]}  ║ "
        for case in row:
            if case == 0:
                temp_line += "◦ "
            elif case == 1:
                temp_line += "  "
            elif case == 2:
                temp_line +=  "■ " 
        grid_drawed += f"\n{temp_line}║ {alphabet_min[(i * 2)]} "
    grid_drawed += "\n   ╚" + "══" * len(grid[0]) + "═╝\n" + "    " + alphabet_maj[0:len(grid[0] * 2)]
    print(grid_drawed)
    return

