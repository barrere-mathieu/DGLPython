import matplotlib.pyplot as plt

# Histograme lettre

f = open("data.txt", "r")
texte = f.readlines()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count = [0]*len(alphabet)

for line in texte:
    if line != "\n":
        for k in range(len(line)):
            lettre = line[k].lower()
            if lettre in alphabet:
                count[alphabet.index(lettre)] += 1

# Occurence des lettres
print(count)

# Graphique
count_tot = sum(count)
plt.bar(alphabet, [round(k/count_tot, 2) for k in count]); plt.show()

