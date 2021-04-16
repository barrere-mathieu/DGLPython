import sys, pygame
import random
from pygame.locals import *
import numpy as np
pygame.init()

########################################################################################################################
# PYGAME SETUP

# Initialize program
pygame.init()

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()

# Setting up color objects
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font
myfont = pygame.font.SysFont("arial", 40)

# Setup a 600x600 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((600, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("TicTacToe1337")

# Creating Lines and Shapes
pygame.draw.line(DISPLAYSURF, BLACK, (200, 0), (200, 600))
pygame.draw.line(DISPLAYSURF, BLACK, (400, 0), (400, 600))
pygame.draw.line(DISPLAYSURF, BLACK, (0, 200), (600, 200))
pygame.draw.line(DISPLAYSURF, BLACK, (0, 400), (600, 400))
########################################################################################################################
# VARIABLES
ORDINATEUR = 1
HUMAIN = 2

tableau = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

victory = 0
end_game = False
tour = 0
IA = 0
#Conversion numéro de case -> place dans la table
coordonates = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}
#Conversion place dans la table -> numéro de case
coordonates_inv = {
    (0, 0): 1,
    (0, 1): 2,
    (0, 2): 3,
    (1, 0): 4,
    (1, 1): 5,
    (1, 2): 6,
    (2, 0): 7,
    (2, 1): 8,
    (2, 2): 9,
}
# Conversion coordonnées écran -> numéro de case
num_case = {
    (100, 100): 1,
    (300, 100): 2,
    (500, 100): 3,
    (100, 300): 4,
    (300, 300): 5,
    (500, 300): 6,
    (100, 500): 7,
    (300, 500): 8,
    (500, 500): 9,
}
# Conversion numéro de case -> coordonnées écran
num_case_inv = {
    1: (100, 100),
    2: (300, 100),
    3: (500, 100),
    4: (100, 300),
    5: (300, 300),
    6: (500, 300),
    7: (100, 500),
    8: (300, 500),
    9: (500, 500),
}
########################################################################################################################
# FUNCTIONS

# Arrondi position
def arrondi_coordonnees(x, y):
    coords = [100, 100]
    diff_x = abs(x - 100)
    if abs(x - 300) < diff_x:
        diff_x = abs(x - 300)
        coords[0] = 300
    if abs(x - 500) < diff_x:
        coords[0] = 500

    diff_y = abs(y - 100)
    if abs(y - 300) < diff_y:
        diff_y = abs(y - 300)
        coords[1] = 300
    if abs(y - 500) < diff_y:
        coords[1] = 500
    return (coords[0], coords[1])

def update_interface(centre):
    if player == 1:
        pygame.draw.circle(DISPLAYSURF, BLUE, centre, 70, 10)
    else:
        pygame.draw.line(DISPLAYSURF, RED, (centre[0] - 50, centre[1] - 50), (centre[0] + 50, centre[1] + 50), 10)
        pygame.draw.line(DISPLAYSURF, RED, (centre[0] - 50, centre[1] + 50), (centre[0] + 50, centre[1] - 50), 10)

def is_possible(table, centre):
    case = num_case[centre]
    x = coordonates[case][0]
    y = coordonates[case][1]
    if table[x][y] == 0:
        return True
    else:
        return False

def update_table(table, joueur, case):
    x = coordonates[case][0]
    y = coordonates[case][1]
    table[x][y] = joueur
    return table

def jouer_coup(table, joueur, case):
    update_table(table, joueur, case)
    update_interface(num_case_inv[case])

def check_end(table):
    try:
        table = table.tolist()
    except:
        pass
    # Check diags
    if table[0][0] == table[1][1] == table[2][2] and table[0][0] != 0:
        victory = table[0][0]
        return victory

    elif table[0][2] == table[1][1] == table[2][0] and table[0][2] != 0:
        victory = table[0][2]
        return victory

    for k in range(len(table)):
        # Check lines
        if table[k][0] == table[k][1] == table[k][2] and table[k][0] != 0:
            victory = table[k][0]
            return victory

        # Check columns
        elif table[0][k] == table[1][k] == table[2][k] and table[0][k] != 0:
            victory = table[0][k]
            return victory

    # Check full board
    if table[0].count(0) + table[1].count(0) + table[2].count(0) == 0:
        return 0
    return
########################################################################################################################
# IA

def possibilities(table):
    available = []
    for x in range(3):
        for y in range(3):
            if table[x][y] == 0:
                available.append(coordonates_inv[(x, y)])
    return available

def scoring_plateau(table, joueur):
    table = table.tolist()

    # Un alignement présente un intérêt si on a la possibilité de gagner
    score = 0
    if joueur == ORDINATEUR:
        adversaire = HUMAIN
    else:
        adversaire = ORDINATEUR

    for k in range(3):
        # Intérêt ligne
        ligne = [table[k][0], table[k][1], table[k][2]].count(adversaire)
        if ligne == 0:
            score += 1
        # Intérêt colonne
        colonne = [table[0][k], table[1][k], table[2][k]].count(adversaire)
        if colonne == 0:
            score += 1
    # Intérêt diagonales
    diag1 = [table[0][0], table[1][1], table[2][2]].count(adversaire)
    diag2 = [table[0][2], table[1][1], table[2][0]].count(adversaire)
    if diag1 == 0:
        score += 1
    if diag2 == 0:
        score += 1
    return score

def valeur_terminale(table):
    return scoring_plateau(table, ORDINATEUR) - scoring_plateau(table, HUMAIN)

def Valeur_MinMax(table, prof, est_max):
    gagne = check_end(table)
    if gagne == ORDINATEUR:
        # print('ordi gagne')
        return 10000
    if gagne == HUMAIN:
        # print('humain gagne')
        return -10000
    if prof == 0:
        return valeur_terminale(table)
    if len(possibilities(table)) == 0:
        return 0

    if est_max:
        #coup possible de l'ordinateur
        resultat = -10001
        for case in possibilities(table):
            #Travailler sur une copie du plateau
            tableau2=np.copy(table)
            #calculer son score à la profondeur donnée
            score = Valeur_MinMax(update_table(tableau2, ORDINATEUR, case),prof - 1, False)
            if score > resultat:
                resultat = score
        return resultat
    else:
        #coup possible du joueur
        resultat = 10001
        for case in possibilities(table):
            #Travailler sur une copie du plateau
            tableau2=np.copy(table)
            #calculer son score à la profondeur donnée
            score = Valeur_MinMax(update_table(tableau2, HUMAIN, case),prof - 1, True)
            if score < resultat:
                resultat = score
        return resultat
    return

def Decision_MinMax(table, profmax):
    resultat = -1
    bscore = -10001
    available = possibilities(table)
    if len(available) > 0:
        for case in available:
            #on calcule la valeur_MinMax pour chaque case du plateau
            tableau2=np.copy(table)
            score = Valeur_MinMax(update_table(tableau2, ORDINATEUR, case),profmax, False)
            # print("score ", score, "case: ", case)
            if score> bscore:
                bscore = score
                resultat = case
                # print("score ", score, "col: ", col)
    print(" choix case :", resultat, "score", bscore)
    return resultat

def choix_IA(table):
    available = possibilities(table)
    if level_IA == 1:
        if random.random() > 0.5:
            i = random.randint(0, len(available) - 1)
            case = available[i]
        else:
            case = Decision_MinMax(table, 1)

    elif level_IA == 2:
        if random.random() > 0.8:
            i = random.randint(0, len(available) - 1)
            case = available[i]
        else:
            case = Decision_MinMax(table,2)

    elif level_IA == 3:
        case = Decision_MinMax(table, 3)

    return case


########################################################################################################################
# GAME
IA = 1          # Présence d'IA (0/1)
level_IA = 3    # Niveau d'IA (1 -> 3)

# Beginning Game Loop
# Random player starts
player = random.randint(1, 2)
tour = 0
while not end_game:
    tour += 1
    coup_valide = False
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if player == ORDINATEUR and IA != 0:
            jouer_coup(tableau, player, choix_IA(tableau))
            player = player % 2 + 1
            print(tableau)
            pygame.display.update()

        if player == HUMAIN or IA == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                centre = arrondi_coordonnees(event.pos[0], event.pos[1])
                if is_possible(tableau, centre):
                    jouer_coup(tableau, player, num_case[centre])
                    player = player % 2 + 1
                    print(tableau)
                    pygame.display.update()
                # print(possibilities(tableau))

        # Check victoire
        victoire = check_end(tableau)
        if victoire == 0:
            texte_image = myfont.render("MATCH NULL", True, BLACK)
            DISPLAYSURF.blit(texte_image, [100, 10])
            pygame.display.update()
            end_game = True
        elif victoire == 1:
            texte_image = myfont.render("Le Joueur O Gagne", True, BLACK)
            DISPLAYSURF.blit(texte_image, [100, 10])
            pygame.display.update()
            end_game = True
        elif victoire == 2:
            texte_image = myfont.render("Le Joueur X Gagne", True, BLACK)
            DISPLAYSURF.blit(texte_image, [100, 10])
            pygame.display.update()
            end_game = True

    FramePerSec.tick(FPS)

pygame.time.wait(1000)
pygame.quit()
sys.exit()
