def arrondi(notes: list = []):
    new_list = []
    for elem in notes:
        try:
            if elem%5 > 2:
                new_list.append(elem - elem%5 + 5)
            else:
                new_list.append(elem)
        except:
            new_list.append(elem)
    return new_list

test_notes = [18, 40, 71, 88, 99, 7]
notes_arrondies_test = arrondi(test_notes)
print(notes_arrondies_test)
