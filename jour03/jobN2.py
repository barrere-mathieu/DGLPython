f = open("data.txt", "r")
texte = f.readlines()
count = 0
for line in texte:
    for k in range(len(line)):
        if k == 0:
            continue
        if line[k-1].isalpha() and not line[k].isalpha():
            # On prend l'hypothère qu'il n'y a pas de caractères spéciaux dans le mot
            # Autrement on peut se servir des librairie comme nltk qui intègrent déjà les habitudes d'écriture
            # Regex en dernier recours
            count += 1
print(count)