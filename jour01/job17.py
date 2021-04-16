j = 0
liste_nombre = []
while j < 5:
    valid = False
    while not valid:
        try:
            n = float(input("Enter a number : "))
            valid = True
        except:
            print("Enter valid number")
    liste_nombre.append(n)
    j += 1

liste_nombre.sort()
print(liste_nombre)