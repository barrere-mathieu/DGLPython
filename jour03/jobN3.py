nombre_input = int(input("Entrez une taille de mot : "))

f = open("data.txt", "r")
texte = f.readlines()
count = 0
taille = 0
for line in texte:
    for k in range(len(line)):
        if line[k].isalpha():
            taille += 1
        if k == 0:
            continue
        if line[k-1].isalpha() and not line[k].isalpha():
            if taille == nombre_input:
                count += 1
            taille = 0

print(count)