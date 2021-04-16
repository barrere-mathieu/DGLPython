import matplotlib.pyplot as plt

# Histograme nombre de mot dans chaque phrase
f = open("data.txt", "r")
texte = f.readlines()

def sentence_size():
    taille = 0
    alphabet = []
    count = []
    ponctuation_fin = [".", "!", "?"]

    for line in texte:
        if line != "\n":
            for k in range(len(line) - 1):
                if line[k].isalpha() and not line[k+1].isalpha():
                    taille += 1
                if line[k] in ponctuation_fin and taille > 0:
                    if taille not in alphabet:
                        # A t-on l'index dans l'alphabet ?
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
    print("Taille des phrases")
    print(alphabet)
    print("Occurence")
    print(count_sort)

    # Graphique
    plt.bar(alphabet, count_sort); plt.xticks(alphabet); plt.show()

