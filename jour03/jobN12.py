import numpy as np

valid = False
while not valid:
    try :
        N = int(input("Renseigner le nombre de cases : "))
        if 4 <= N <= 10:
            valid = True
        else:
            print('Erreur ! Entrez un entier compris entre 4 et 10\n')
    except:
        print('Erreur ! Entrez un entier compris entre 4 et 10\n')

TABLE = []
for k in range(N):
    TABLE.append([0]*N)
RESULTAT = []
# ----------------------------------------------------------------------------------------------------------------------

def afficher_plateau(table):
    affichage = []
    table = table.tolist()
    for L in table:
        ligne = "".join([str(i) + " " for i in L])
        ligne = ligne.replace("2", "X")
        ligne = ligne.replace("1", "O")
        ligne = ligne.replace("0", "O")
        affichage.append("".join(ligne))
        affichage.append("\n")
    print("".join([ligne for ligne in affichage]))

def is_inRange(n):
    if 0 <= n <= N-1:
        return True
    else:
        return False

def placer_reines(table, x, y):
    for k in range(N):
        table[x][k] = 1
        table[k][y] = 1
        if k > 0:
            if is_inRange(x-k) and is_inRange(y-k):
                table[x-k][y-k] = 1
            if is_inRange(x-k) and is_inRange(y+k):
                table[x-k][y+k] = 1
            if is_inRange(x+k) and is_inRange(y-k):
                table[x+k][y-k] = 1
            if is_inRange(x+k) and is_inRange(y+k):
                table[x+k][y+k] = 1
    table[x][y] = 2
    return table

def places_dispo(table):
    # Repérer les coordonnées des reines
    dispo = []
    for l in range(N):
        for c in range(N):
            if table[l][c] == 0:
                dispo.append((l, c))
    return dispo

def recursive(table, prof):
    dispo = places_dispo(table)
    if prof == 0:
        RESULTAT.append(table)
        # Retourne tous les résultats
        # return []

        # Retourne uniquement le premier résultat trouvé pour une position initiale donnée
        return table

    if dispo == []:
        return []

    for coord in dispo:
        x = coord[0]
        y = coord[1]
        table2 = np.copy(table)
        resultat = recursive(placer_reines(table2, x, y), prof-1)
        if resultat != []:
            return resultat
    return []

def algo():
    dispo = places_dispo(TABLE)
    for coord in dispo:
        x = coord[0]
        y = coord[1]
        # print("Coords = (", x, ",", y, ")")
        table = np.copy(TABLE)
        recursive(placer_reines(table, x , y), N-1)
    return

algo()
for table in RESULTAT:
    print('--------------------------------------------')
    afficher_plateau(table)
print(len(RESULTAT))
