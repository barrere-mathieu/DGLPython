from numpy.random import choice
from jobN5 import word_size
from jobN6 import first_letter
from jobN7 import next_letter
from jobN9 import sentence_size

f = open("data.txt", "r")
texte = f.readlines()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# Generateur de mot

def init():
    a, b = word_size()
    print("1/4")
    c = first_letter()
    print("2/4")
    d = next_letter()
    print("3/4")
    e, f = sentence_size()
    print("4/4")
    return a, b, c, d, e, f

def gen_mot(all_size, prob_size, first_letter, next_letter, is_first):
    # Roll size
    size = int(choice(all_size, 1, p = prob_size))
    # Roll 1st letter
    word = [str(choice(alphabet, 1, p = first_letter)[0])]
    L_before = word[0]
    if is_first:
        word[0] = word[0].upper()
    for p in range(size-1):
        L = str(choice(alphabet, 1, p = next_letter[alphabet.index(L_before)])[0])
        word.append(L)
        L_before = L
    return "".join(word)

def gen_phrase(all_size, prob_size, first_letter, next_letter, sentence_all_size, sentence_prob):
    # Roll size
    size = int(choice(sentence_all_size, 1, p = sentence_prob))
    sentence = []
    for w in range(size):
        is_first = False
        if w == 0:
            is_first = True
        sentence.append(gen_mot(all_size, prob_size, first_letter, next_letter, is_first))
        if w == size -1:
            sentence.append('.')
        else:
            sentence.append(' ')
    return "".join(sentence)

if __name__ == "__main__":
    print("Start init")
    # Pas optimisé car on parcourt le texte 4 fois -> volontée de réutiliser le code des précédents exercices
    all_size, prob_size, first_letter, next_letter, sentence_all_size, sentence_prob = init()
    print("End init\n")
    for k in range(10):
        print(gen_phrase(all_size, prob_size, first_letter, next_letter, sentence_all_size, sentence_prob))
