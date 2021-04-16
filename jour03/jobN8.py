from numpy.random import choice
from jobN5 import word_size
from jobN6 import first_letter
from jobN7 import next_letter

f = open("data.txt", "r")
texte = f.readlines()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# Generateur de mot

def init():
    a, b = word_size()
    print("1/3")
    c = first_letter()
    print("2/3")
    d = next_letter()
    print("3/3")
    return a, b, c, d

def gen_mot(all_size, prob_size, first_letter, next_letter):
    # Roll size
    size = int(choice(all_size, 1, p = prob_size))
    # Roll 1st letter
    word = [str(choice(alphabet, 1, p = first_letter)[0])]
    L_before = word[0]
    for p in range(size-1):
        L = str(choice(alphabet, 1, p = next_letter[alphabet.index(L_before)])[0])
        word.append(L)
        L_before = L
    word[0].upper()
    return "".join(word)

if __name__ == "__main__":
    print("Start init")
    # Pas optimisé car on parcourt le texte 3 fois -> volontée de réutiliser le code des précédents exercices
    all_size, prob_size, first_letter, next_letter = init()
    print("End init\n")
    for k in range(10):
        print(gen_mot(all_size, prob_size, first_letter, next_letter))