import matplotlib.pyplot as plt

# Histograme lettre début de mot
f = open("data.txt", "r")
texte = f.readlines()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def first_letter():
    count = [0]*len(alphabet)

    for line in texte:
        if line != "\n":
            for k in range(len(line)):
                if k == 0:
                    continue
                if line[k].isalpha() and not line[k-1].isalpha():
                    lettre = line[k].lower()
                    if lettre in alphabet:
                        count[alphabet.index(lettre)] += 1

    count_tot = sum(count)
    return [k/count_tot for k in count]

if __name__ == "__main__":
    count_pct = first_letter()

    # Occurence des lettres
    print(count_pct)
    print(sum(count_pct))

    # Graphique
    plt.bar(alphabet, count_pct); plt.show()

