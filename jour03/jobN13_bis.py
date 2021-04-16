import csv
import re

# Same with regex: much longer to compute
csvfile = open('pokemon.csv', 'r')
reader = csv.reader(csvfile, delimiter = ',')
pokemons = []
for element in reader:
    pokemons.append(element[1].lower())

f = open("data.txt", "r")
texte = f.readlines()
for line in texte:
    if line != "\n" and len(line) > 1:
        line = line.lower()
        for p in pokemons:
            reg_expr = r'([ !@#$%^&*()[]{};:,./<>?\|`~-=_+])'+p+'([ !@#$%^&*()[]{};:,./<>?\|`~-=_+])'
            if re.findall(reg_expr, line) != []:
                print("Pokemon trouvé : ", p)

