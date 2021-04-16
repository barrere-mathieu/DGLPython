import matplotlib.pyplot as plt

# Histograme taille de mot
f = open("data.txt", "r")
texte = f.readlines()

def word_size():
    taille = 0
    alphabet = []
    count = []

    for line in texte:
        if line != "\n":
            for k in range(len(line)):
                if line[k].isalpha():
                    taille += 1
                if k == 0:
                    continue
                if line[k - 1].isalpha() and not line[k].isalpha():
                    # A t-on l'index dans l'alphabet ?
                    if taille not in alphabet:
                        alphabet.append(taille)
                        count.append(0)
                    count[alphabet.index(taille)] += 1
                    taille = 0

    sort_indexes = sorted(range(len(alphabet)), key=lambda k: alphabet[k])
    alphabet.sort()
    count_tot = sum(count)
    count_sort = [count[k]/count_tot for k in sort_indexes]
    return alphabet, count_sort

if __name__ == "__main__":
    alphabet, count_sort = word_size()
    # Occurence des lettres
    print("Taille des mots")
    print(alphabet)
    print("Occurence")
    print(count_sort)

    # from numpy.random import choice
    # for k in range(10):
    #     size = choice(alphabet, 1, p=count_sort)
    #     print(size)

    # Graphique
    plt.bar(alphabet, count_sort); plt.xticks(alphabet); plt.show()

