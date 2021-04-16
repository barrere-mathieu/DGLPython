import csv

csvfile = open('pokemon.csv', 'r')
reader = csv.reader(csvfile, delimiter = ',')
pokemons = []
for element in reader:
    pokemons.append(" "+element[1].lower()+" ")

f = open("data.txt", "r")
texte = f.readlines()
for line in texte:
    if line != "\n" and len(line) > 1:
        line = line.lower()
        for p in pokemons:
            if line.find(p) > -1:
                print("Pokemon trouvé : ", p)

