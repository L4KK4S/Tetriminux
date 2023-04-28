"""
##########################################

Projet : Création jeux Tetris
Groupe TD: A
Membre: Abdel-Waheb Sakkal; Thomas Dos Santos

##########################################
"""

import time
from other import regles
import create_plate
import plate
import bloc
import position
import score
import Column_Row

def game():


    # print the title
    title ="_____ _____ _____ ____  ___ __  __ ___ _   _ _   ___  __\n|_  _| ____|_   _|  _ \|_ _|  \/  |_ _| \ | | | | \ \/ /\n | | |  _|   | | | |_) || || |\/| || ||  \| | | | |\  / \n | | | |___  | | |  _ < | || |  | || || |\  | |_| |/  \ \n |_| |_____| |_| |_| \_\___|_|  |_|___|_| \_|\___//_/\_\ \n                                     by Lakkas & thom_dos\n\n"
    print(title)
    time.sleep(1)
    print("BIENVENUE SUR TETRIMINUX !\n")
    time.sleep(0.5)

    # asks for game or rules
    print("1. Nouvelle Partie \n2. Voir les règles\n3. Continuer la partie sauvegardée")
    initial_choice = input(">>> ")
    while initial_choice not in ["1", "2", "3"]:
        initial_choice = input("Cette valeur n'est pas acceptée ! \n>>> ")
    time.sleep(0.5)

    if initial_choice == "2":
        print(regles)
        time.sleep(2)
        print("\nEntrez 1 pour commencer à jouer")
        initial_choice = input(">>> ")
        while initial_choice != "1":
            initial_choice = input("Cette valeur n'est pas acceptée ! \n>>> ")


    if initial_choice == "1":

        # asks for shape
        print("\n1. Losange\n2. Cercle\n3. Triangle")
        shape_choice = input(">>> ")
        while shape_choice not in ["1", "2", "3"]:
            shape_choice = input("Cette valeur n'est pas acceptée ! \n>>> ")
        time.sleep(0.5)

        # asks for shape size
        print("\nEntrez la taille de la grille de jeu")
        plate_size = input(">>> ")
        while plate_size not in ["21", "22", "23", "24", "25", "26"]:
            plate_size = input("Cette valeur n'est pas acceptée ! \n>>> ")
        time.sleep(0.5)

        create_plate.creation_plateau(shape_choice, int(plate_size)) # generates the platr in a txt file
        current_plate = plate.read_grid('current_game.txt') # creates the matrix of the plate
        score_ = 0

    elif initial_choice == "3":
        current_plate = plate.read_grid('saved_game.txt')
        plate_size = len(current_plate)
        with open('saved_game_data.txt') as f:
            lines = f.readlines()
            shape_choice = lines[0][0]
            score_ = int(lines[1])

    lives, case = 3, 0
    run = True
    while run:


        alphabet = "abcdefghijklmnopqrstuvwxyz"[:int(plate_size)]  # the valid case to choose
        alphabet2 = "abcdefghijklmnopqrstuvwxyz"[:int(len(current_plate[0]))]

        print(f"\n {' ' * (int(plate_size) // 2 )}       |SCORE : {score_}|")
        plate.print_grid(current_plate)  # diplays the game
        blocks_choice_list = bloc.draw_choices(shape_choice) # generates the list of the avaiable blocks

        # asks for play or save
        print("\n1. Jouer\n2. Sauvegarder")
        save_game = input(">>> ")
        while save_game not in ["1", "2"]:
            save_game = input("Cette valeur n'est pas acceptée ! \n>>> ")
        time.sleep(0.5)

        if save_game == "2": # exit if we want to save
            plate.save_grid("saved_game.txt", current_plate, shape_choice, score_)
            case = 1
            run = False
            break

        print("\nChoisissez le bloc à placer") # the player have to choose one
        choice_nb = input(">>> ")
        while choice_nb not in ["1", "2", "3"]:
            choice_nb = input("Cette valeur n'est pas acceptée ! \n>>> ")
        time.sleep(0.5)
        choosen_block = blocks_choice_list[int(choice_nb) - 1]

        can_be_placed = False # if we can place a piece
        while can_be_placed is False and lives != 0:
            if shape_choice == "3":
                i, j = position.choix_position(alphabet, alphabet2)
                x, y = alphabet.index(i), alphabet2.index(j)
            else:
                i, j = position.choix_position(alphabet)
                x, y = alphabet.index(i), alphabet.index(j)
            can_be_placed = position.valid_position(current_plate, choosen_block, x, y)
            if lives != 0 and can_be_placed is False:
                lives -= 1
                print(f"Ces coordonnées ne sont pas convenables, il vous reste {lives} vies\n")


        if lives == 0: # exit if there are no more lives
            run = False
        else: # else set the number of lives at 3
            lives = 3

        current_plate = position.emplace_bloc(current_plate, choosen_block, x, y) # actualises the plate
        score_ += score.count_pt(choosen_block) # actualises the score

        for row in range(x-4,x+1): # actualises the score if there are lines full
            if Column_Row.row_state(current_plate, row):
                current_plate, nb_cases = Column_Row.row_clear(current_plate, row)
                score_ += nb_cases

        for col in range(y,y+5): # actualises the score if there are columns full
            if Column_Row.col_state(current_plate, col) and col<len(alphabet2):
                current_plate, nb_cases = Column_Row.col_clear(current_plate, col)
                score_ += nb_cases

    if case == 0:
        fin="   ____ _____ _____ ___  ___     ____ _   _____  _____\n  / __ `/ __ `/ __ `__ \/ _ \   / __ \ | / / _ \/ ___/ \n / /_/ / /_/ / / / / / /  __/  / /_/ / |/ /  __/ /  \n \__, /\__,_/_/ /_/ /_/\___/   \____/|___/\___/_/ \n ____/"
        print(fin)
        time.sleep(0.5)
        print("Votre score: ",score_)
    else:
        print(f"\n\n LA PARTIE A ETE SAUVEGARDEE LE SCORE EST DE {score_}")

game()






