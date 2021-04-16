import random
class Board():
    def __init__(self, largeur: int = 10, longueur: int = 10):
        self.largeur = max(largeur, 4)
        self.longueur = max(longueur, 4)
        self.table = []
        for k in range(longueur):
            self.table.append([0]*largeur)

    def __str__(self):
        affichage = []
        for ligne in self.table:
            affichage.append("".join([str(i) + " " for i in ligne]))
            affichage.append("\n")
        return "".join([ligne for ligne in affichage])


# ---------------------------------------------------------------------------------------------------------------------#
class Bateau(object):
    def __init__(self, type, taille):
        self.type = type
        self.taille = taille
        self.pv = [1]*taille
        self.position_x = []
        self.position_y = []

    def assessment(self, ligne, colonne):
        pv_restant = self.pv.count(1)
        if ligne in self.position_x and colonne in self.position_y:
            self.pv[-pv_restant] = 0

    def is_dead(self):
        if sum(self.pv) == 0:
            return True
        else:
            return False

    def __str__(self):
        return self.type + ' : ' + str(self.pv)

class Porte_avion(Bateau):
    def __init__(self):
        super(Porte_avion, self).__init__("Porte-avion", 4)
class Fregate(Bateau):
    def __init__(self):
        super(Fregate, self).__init__("Frégate", 3)
class Cotier(Bateau):
    def __init__(self):
        super(Cotier, self).__init__("Côtier", 2)

# ---------------------------------------------------------------------------------------------------------------------#
class Joueur(object):
    def __init__(self, status, num):
        self.status = status # 1 -> IA | 0 -> Humain
        self.num = num
        self.flotte = []
        self.board = Board
        self.adversaire = Board

    def is_dead(self):
        count = 0
        for bateau in self.flotte:
            if bateau.is_dead():
                count += 1
        if count == len(self.flotte):
            return True

    def add_boat(self, bateau):
        self.flotte.append(bateau)

    def etat_flotte(self):
        print('Joueur', self.num, "- Etat de la flotte :")
        for k in self.flotte:
            print(k)

    def available(self, direction, bateau):
        ligne_dispo = []
        colonne_dispo = []

        if direction == 0:
            # Direction horizontale
            # -> donne une liste de ligne avec suffisemment de place pour le bateau
            # -> donne une liste de colonne pour chaque ligne
            for ligne in range(self.board.longueur):
                temp = []
                for colonne in range(self.board.largeur + 1 - bateau.taille):
                    if sum([int(self.board.table[ligne][colonne + k]) for k in range(bateau.taille)]) == 0:
                        temp.append(colonne)
                if temp != []:
                    colonne_dispo.append(temp)
                    ligne_dispo.append(ligne)
        if direction == 1:
            # Vertical
            for colonne in range(self.board.largeur):
                temp = []
                for ligne in range(self.board.longueur + 1 - bateau.taille):
                    if sum([int(self.board.table[ligne + k][colonne]) for k in range(bateau.taille)]) == 0:
                        temp.append(ligne)
                if temp != []:
                    ligne_dispo.append(temp)
                    colonne_dispo.append(colonne)
        return ligne_dispo, colonne_dispo

    def positionner_bateau(self):
        for bateau in self.flotte:
            place = False
            while not place:
                direction = random.randint(0, 1)
                if direction == 0:
                    # Horizontal
                    ligne_dispo, colonne_dispo = self.available(direction, bateau)
                    if ligne_dispo != []:
                        start_x = random.choice(ligne_dispo)
                        start_y = random.choice(colonne_dispo[ligne_dispo.index(start_x)])
                        for k in range(bateau.taille):
                            self.board.table[start_x][start_y + k] = 1
                            bateau.position_x.append(start_x)
                            bateau.position_y.append(start_y + k)
                        place = True
                    else:
                        direction = 1
                if direction == 1:
                    # Vertical
                    ligne_dispo, colonne_dispo = self.available(direction, bateau)
                    if ligne_dispo != []:
                        start_y = random.choice(colonne_dispo)
                        start_x = random.choice(ligne_dispo[colonne_dispo.index(start_y)])
                        for k in range(bateau.taille):
                            self.board.table[start_x + k][start_y] = 1
                            bateau.position_x.append(start_x + k)
                            bateau.position_y.append(start_y)
                        place = True
                    else:
                        direction = 0

    def update_attaque(self, plateau_adverse, ligne, colonne):
        if plateau_adverse.table[ligne][colonne] == 1:
            self.adversaire.table[ligne][colonne] = 2
            print("Touché !")
        elif plateau_adverse.table[ligne][colonne] == 0:
            self.adversaire.table[ligne][colonne] = "X"
            print("Dans l'eau !")
        else:
            print("Coup déjà joué !")
        print("------------------------------\n")


    def update_defense(self, ligne, colonne):
        if self.board.table[ligne][colonne] == 1:
            self.board.table[ligne][colonne] = 2
        for bateau in self.flotte:
            bateau.assessment(ligne, colonne)

class Humain(Joueur):
    def __init__(self, num = 1):
        self.flotte = []
        self.board = Board
        super(Humain, self).__init__(0, num)

    def think(self):
        print("\n------------------------------")
        print("Joueur", self.num, ", à vous :")
        print("------------------------------")
        self.etat_flotte()
        print("------------------------------")
        print(self.adversaire)
        print("------------------------------")

        # Ligne
        valid = False
        while not valid:
            try:
                print("Lignes comprises entre 1 et ", self.board.longueur)
                ligne = int(input('Ligne :'))
                if 1 <= ligne <= self.board.longueur:
                    valid = True
                    ligne = ligne - 1
            except:
                print("Ligne incorrecte")

        # Colonne
        valid = False
        while not valid:
            try:
                print("Colonnes comprises entre 1 et ", self.board.largeur)
                colonne = int(input('Colonne :'))
                if 1 <= colonne <= self.board.largeur:
                    valid = True
                    colonne = colonne - 1
            except:
                print("Colonne incorrecte")
        print("------------------------------")

        return ligne, colonne

class IA(Joueur):
    def __init__(self):
        super(IA, self).__init__(1, 2)
        self.flotte = []
        self.board = Board

    def think(self):
        print("\n------------------------------")
        print("Tour de l'IA ...")
        ligne = random.choice(range(self.board.longueur))
        col = random.choice(range(self.board.largeur))
        print('Ligne:', ligne + 1,' | Colonne:', col + 1)
        # Ajouter une mémoire pour ne pas rejouer les mêmes coups

        return ligne, col

# ---------------------------------------------------------------------------------------------------------------------#
class BattleShip():
    def __init__(self, largeur: int = 10, longueur: int = 7, adversaire_IA = 0):
        largeur = max(largeur, 4)
        longueur = max(longueur, 4)
        self.tour = 0
        self.fin = False

        # Init joueurs
        if adversaire_IA == 0:
            self.j1 = Humain(1)
            self.j2 = Humain(2)
        else:
            self.j1 = Humain()
            self.j2 = IA()
        self.j1.board = Board(largeur, longueur)
        self.j1.adversaire = Board(largeur, longueur)
        self.j2.board = Board(largeur, longueur)
        self.j2.adversaire = Board(largeur, longueur)

        # Init flottes
        nombre_bateau = int(0.09*largeur*longueur)
        pa = max(1, int(0.17*nombre_bateau))
        freg = max(1, int(0.5*nombre_bateau))
        cot = max(1, nombre_bateau - pa - freg)
        for add in range(3):
            count = [pa, freg, cot][add]
            while count != 0:
                if add == 0:
                    self.j1.add_boat(Porte_avion())
                    self.j2.add_boat(Porte_avion())
                elif add == 1:
                    self.j1.add_boat(Fregate())
                    self.j2.add_boat(Fregate())
                elif add == 2:
                    self.j1.add_boat(Cotier())
                    self.j2.add_boat(Cotier())
                count -= 1
        self.j1.positionner_bateau()
        self.j2.positionner_bateau()
        self.lancer_partie()

    def is_over(self, joueur):
        if joueur.is_dead():
            self.fin = True
            print("Joueur", joueur.num%2 + 1, "à gagné !")

    def lancer_partie(self):
        joueurs = [self.j1, self.j2]
        joueur_actif = random.randint(1, 2)
        while not self.fin:
            self.tour += 1
            joueur = joueurs[int(joueur_actif - 1)]
            adversaire = joueurs[2 - joueur_actif]
            plateau_adverse = adversaire.board

            ligne, colonne = joueur.think()
            joueur.update_attaque(plateau_adverse, ligne, colonne)
            adversaire.update_defense(ligne, colonne)
            self.is_over(adversaire)
            joueur_actif = joueur_actif%2 + 1


p = BattleShip(largeur = 10, longueur = 7, adversaire_IA = 1)
