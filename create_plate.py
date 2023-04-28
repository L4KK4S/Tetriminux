def plateau_triangle(taille):
    """
            Create a txt file with triangular plate
            :param: taille
            :type : int
            :return:
            :rtype:
            :Example:
                 >>> plateau_triangle(5)
                    current_game.txt:
                    1 1 0 1 1
                    1 0 0 0 1
                    0 0 0 0 0
    """
    plateau= open("current_game.txt","w")
    i=0
    while i*2+1<taille-1:
        ligne= "1 "*((taille-(i*2+1))//2) + "0 "*(i*2+1) + "1 "*((taille-(i*2+1))//2)
        plateau.write(ligne + "\n")
        i+=1
    ligne = "1 " * ((taille - (i * 2 + 1)) // 2) + "0 " * (i * 2 + 1) + "1 " * ((taille - (i * 2 + 1)) // 2)
    plateau.write(ligne)
    plateau.close()
    return

def plateau_losange(taille):
    """
                Create a txt file with diamond plate
                :param: taille
                :type : int
                :return:
                :rtype:
                :Example:
                     >>> plateau_losange(5)
                        current_game.txt:
                        1 1 0 1 1
                        1 0 0 0 1
                        0 0 0 0 0
                        1 0 0 0 1
                        1 1 0 1 1
        """
    plateau = open("current_game.txt", "w")
    i = 0
    while i * 2 + 1 < taille:
        ligne = "1 " * ((taille - (i * 2 + 1)) // 2) + "0 " * (i * 2 + 1) + "1 " * ((taille - (i * 2 + 1)) // 2)
        plateau.write(ligne + "\n")
        i += 1
    i-=1
    while i>=1:
        ligne = "1 " * ((taille - (i * 2 + 1)) // 2) + "0 " * (i * 2 + 1) + "1 " * ((taille - (i * 2 + 1)) // 2)
        plateau.write(ligne + "\n")
        i -= 1
    ligne = "1 " * ((taille - (i * 2 + 1)) // 2) + "0 " * (i * 2 + 1) + "1 " * ((taille - (i * 2 + 1)) // 2)
    plateau.write(ligne)
    plateau.close()
    return

def plateau_cercle(taille):
    """
                Create a txt file with circle plate
                :param: taille
                :type : int
                :return:
                :rtype:
                :Example:
                     >>> plateau_cercle(5)
                        current_game.txt:
                        1 0 0 0 1
                        0 0 0 0 0
                        0 0 0 0 0
                        0 0 0 0 0
                        1 0 0 0 1
        """
    plateau = open("current_game.txt", "w")
    Exterieur = taille // 5
    Interieur = taille - (Exterieur * 2)
    Vide = Exterieur
    zone_jeux = Interieur
    while Vide > 0:
        plateau.write(Vide * '1 ' + zone_jeux * '0 ' + Vide * '1 '+"\n")
        Vide -= 1
        zone_jeux += 2
    for j in range(Interieur):
        plateau.write(taille * '0 '+"\n")
    while Vide < Exterieur-1:
        Vide += 1
        zone_jeux -= 2
        plateau.write(Vide * '1 ' + zone_jeux * '0 ' + Vide * '1 '+"\n")
    Vide += 1
    zone_jeux -= 2
    plateau.write(Vide * '1 ' + zone_jeux * '0 ' + Vide * '1 ')
    plateau.close()
    return

def creation_plateau(forme_plateau,taille_plateau):
    """
                    call one of the functions according to the player's choice
                    :param: forme_plateau,taille_plateau
                    :type : str,int
                    :return: /
                    :rtype: /
                    :Example:
                         >>> creation_plateau('2',5)
                            plateau_cercle(5)
            """
    if forme_plateau=="3":
        plateau_triangle(taille_plateau)
    elif forme_plateau=="2":
        plateau_cercle(taille_plateau)
    else:
        plateau_losange(taille_plateau)
    return



