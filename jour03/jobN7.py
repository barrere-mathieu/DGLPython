import matplotlib.pyplot as plt

# Histograme lettre suivante
f = open("data.txt", "r")
texte = f.readlines()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def next_letter():
    count = []
    count_pct = []
    for i in range(len(alphabet)):
        count.append([0]*len(alphabet))
        count_pct.append([0]*len(alphabet))
    count_tot = []

    for line in texte:
        if line != "\n" and len(line) > 1:
            for k in range(len(line)-1):
                if line[k].isalpha() and line[k+1].isalpha():
                    lettre0 = line[k].lower()
                    lettre1 = line[k+1].lower()
                    if lettre0 == 'w':
                        stop = 1
                    if lettre0 in alphabet and lettre1 in alphabet:
                        count[alphabet.index(lettre0)][alphabet.index(lettre1)] += 1

    for k in count:
        count_tot.append(sum(k))
    for i in range(len(alphabet)):
        if count_tot[i] != 0:
            for j in range(len(alphabet)):
                count_pct[i][j] = count[i][j] / count_tot[i]
    return count_pct

if __name__ == "__main__":

    # Graphique
    count_pct = next_letter()
    for y_arr, label in zip(count_pct, alphabet):
        plt.plot(alphabet, y_arr, label = label)
    plt.legend()
    plt.show()

