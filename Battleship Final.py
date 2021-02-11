import random

board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]

guesses_board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]


lettres = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]# Liste des lettres disponibles sur le plateau
liste_bateaux_ai = []# Liste des Objets Bateau (La classe juste en dessous)
bateaux_size = [5, 4, 3, 3, 2, 2]# Tous les Bateau de l'IA (le chiffre représente la taille de 2 à 5)
global_pos = []
liste_bateaux_player = []


class Bateau:  # Class bateau
    def __init__(self, pos, mode):  #  Initialisation de l'objet c'est la qu'il prend ces positions et son mode (vertical, horizontal)
        self.pos = pos  # Tableau de position
        self.mode = mode  # 0 ou 1 selon vertical ou horizontal
        self.touched = []  # les positions touchés pas le joueur
        self.killed = False  # si le bateau est mort

    def check_touched(self, pos, IA):  #  ici on regardes si le bateau est touché par la position indiqué par l'utilisateur dans game
        if not self.killed:
            if pos in self.pos:
                self.touched.append(pos)
                if IA:
                    print("l'IA a touché un de vos bateaux")
                else:
                    print("Touché")
                self.check_killed(IA)
                return True
            else:
                return False

    def check_killed(self, IA):  # Ici on regardes si le bateau est dead
        if len(self.touched) == len(self.pos):
            if IA:
                print("L'IA a coulé un de vos bateaux")
            else:
                print("Coulé")
            self.killed = True

    def is_killed(self):  # cette fonction c'est pour eviter un ralentissement en retirant les bateaux
        if len(self.touched) == len(self.pos):
            return True
        else:
            return False

def setup():  # on setup la position random des bateaux ici
    global_pos_player = []  # ce tableau contient toutes les pos deja utilisées par tes bateaux
    global_pos_ai = []  # ce tableau contient toutes les pos deja utilisées par tes bateaux
    for isize in bateaux_size: # on parcourt ton tableau de taille de bateau
        check_pass = True
        while check_pass:
            check_pass = True
            modec = random.randint(0, 1) # random du mode vertical ou horizontal
            current_pos = []
            # si le bateau est à l'horizontal
            if modec == 0:
                chiffrec1 = random.randint(0, 9)
                rand_int = random.randint(0, 9) #on tire un chiffre aléatoirement en choissisant une lettre et un chiffre ça permet de pas avoir 2 bateaux sur la même position
                indexc1 = rand_int
                lettrec1 = lettres[rand_int]
                if lettrec1 + str(chiffrec1) in global_pos:
                    current_pos.clear()
                    rand_int = -1
                else:
                    check_pass = False
                if not check_pass:
                    current_pos.append(lettrec1 + str(chiffrec1))
                    global_pos.append(lettrec1 + str(chiffrec1))
                    if indexc1 > 4:
                        for iterate in range(isize-1):
                            rand_int -= 1
                            if lettres[rand_int] + str(chiffrec1) in global_pos:
                                current_pos.clear()
                                check_pass = True
                                del global_pos[-(iterate + 1):]
                                break
                            else:
                                check_pass = False
                            current_pos.append(lettres[rand_int] + str(chiffrec1))
                            global_pos.append(lettres[rand_int] + str(chiffrec1))
                    elif 0 <= indexc1 <= 4:
                        for iterate in range(isize-1):
                            if lettres[rand_int] + str(chiffrec1) in global_pos:
                                current_pos.clear()
                                check_pass = True
                                del global_pos[-(iterate + 1):]
                                break
                            else:
                                check_pass = False
                            rand_int += 1
                            current_pos.append(lettres[rand_int] + str(chiffrec1))
                            global_pos.append(lettres[rand_int] + str(chiffrec1))
            # si le bateau est à la vertical
            else:
                chiffrec1 = random.randint(0, 9)
                indexc1 = chiffrec1
                rand_int = random.randint(0, 9)
                lettrec1 = lettres[rand_int]
                if lettrec1 + str(chiffrec1) in global_pos:
                    current_pos.clear()
                    rand_int = -1
                else:
                    check_pass = False
                if not check_pass:
                    current_pos.append(lettrec1 + str(chiffrec1))
                    global_pos.append(lettrec1 + str(chiffrec1))
                    if indexc1 > 4:
                        for iterate in range(isize-1):
                            chiffrec1 -= 1
                            if lettres[rand_int] + str(chiffrec1) in global_pos:
                                current_pos.clear()
                                del global_pos[-(iterate + 1):]
                                check_pass = True
                                break
                            else:
                                check_pass = False
                            current_pos.append(lettres[rand_int] + str(chiffrec1))
                            global_pos.append(lettres[rand_int] + str(chiffrec1))
                    elif 0 <= indexc1 <= 4:
                        for iterate in range(isize-1):
                            chiffrec1 += 1
                            if lettres[rand_int] + str(chiffrec1) in global_pos:
                                current_pos.clear()
                                del global_pos[-(iterate + 1):]
                                check_pass = True
                                break
                            else:
                                check_pass = False
                            current_pos.append(lettres[rand_int] + str(chiffrec1))
                            global_pos.append(lettres[rand_int] + str(chiffrec1))
            if not check_pass:
                liste_bateaux_ai.append(Bateau(current_pos, modec))


letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,

}

def ask_user_for_board_position(): # les deux questions qui va permettre de faire nos tirs
    
    column = input("colonne (A à J):")
    while column not in "ABCDEFGHIJ":
        print("Cette colonne est fausse ! Elle doit être A, B, C, D, E, F, G, H, I ou J")
        column = input("colonne (A à J):")

    row = input("ligne (0 à 9):")
    while row not in "0123456789":
        print("Cette ligne est fausse ! Elle doit être 0, 1, 2, 3, 4, 5, 6, 7, 8 ou 9")
        row = input("ligne (0 à 9):")

    return int(row) , letters_to_numbers[column]


def print_board(board): #Le tableau
    print("  A B C D E F G H I J")
    print(" .-.-.-.-.-.-.-.-.-.-.")
    row_number = 0
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        print(" .-.-.-.-.-.-.-.-.-.-.")
        row_number = row_number + 1

def check_win():  # fonction pour savoir si le joueur à gagné
    count_ai = 0
    count_p = 0
    for bateau in liste_bateaux_ai:
        if bateau.is_killed():
            count_ai += count_ai
    for bateau in liste_bateaux_player:
        if bateau.is_killed():
            count_p += count_p
    if count_ai == len(bateaux_size) or count_p == len(bateaux_size):
        return True
    else:
        return False

def game():  # fonction qui permet de dérouler le jeu dans le bon ordre
    player_guess = []  # tableau de toutes les position deja ecrite par le joueur
    ai_guess = []  # tableau de toutes les position deja ecrite par l'ia
    setup()
    while not check_win():
        print("Player Board")
        print_board(board)
        print_board(guesses_board)
        wrong_input = True
        while wrong_input:
            current_pos = input("Position (Exemple : A2) : ")
            current_pos = list(current_pos)
            if len(current_pos) == 2:
                try:
                    row = int(current_pos[1])
                except TypeError:#Permet d'éviter les soucis si l'on met 2A au lieu de A2
                    wrong_input = True
                    continue
                if current_pos[0].lower() in lettres and 0 <= row <= 9:
                    current_pos = "".join(current_pos).lower()
                    if current_pos in player_guess:
                        print("Tu as déjà donné cette position")
                        wrong_input = True
                    else:
                        check = False
                        for bateau in liste_bateaux_ai:
                            check = bateau.check_touched(current_pos, False)
                            if check:
                                current_pos = list(current_pos)
                                col = lettres.index(current_pos[0])
                                row = int(current_pos[1])
                                guesses_board[row][col] = "X"
                                break
                        if not check:
                            current_pos = list(current_pos)
                            col = lettres.index(current_pos[0])
                            row = int(current_pos[1])
                            guesses_board[row][col] = "O"
                            print("Manqué")
                        wrong_input = False
                else:
                    print("Position non valide")
                    wrong_input = True
            else:
                wrong_input = True
        # IA Turn
        wrong_input = True
        while wrong_input:
            chiffre = random.randint(0, 9)
            rand_int = random.randint(0, 9)
            lettre = lettres[rand_int]
            current_pos = lettre + str(chiffre)
            if current_pos in ai_guess:
                wrong_input = True
            else:
                check = False
                for bateau in liste_bateaux_player:
                    check = bateau.check_touched(current_pos, True)
                    if check:
                        current_pos = list(current_pos)
                        col = lettres.index(current_pos[0])
                        row = int(current_pos[1])
                        board[row][col] = "X"
                        break
                if not check:
                    current_pos = list(current_pos)
                    col = lettres.index(current_pos[0])
                    row = int(current_pos[1])
                    board[row][col] = "O"
                    print("L'IA a Manqué")
                wrong_input = False
    print("You win!")

game()
