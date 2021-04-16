f = open("output.txt", "r")
texte = f.readlines()
for k in texte:
    print(k)
f.close()