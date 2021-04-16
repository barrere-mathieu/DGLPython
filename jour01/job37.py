# Fonction de permutation récupérée sur une librairie open source
# def permutations(iterable, r=None):
#     pool = tuple(iterable)
#     n = len(pool)
#     r = n if r is None else r
#     if r > n:
#         return
#     indices = list(range(n))
#     cycles = list(range(n, n-r, -1))
#     yield "".join(tuple(pool[i] for i in indices[:r]))
#     while n:
#         for i in reversed(range(r)):
#             cycles[i] -= 1
#             if cycles[i] == 0:
#                 indices[i:] = indices[i+1:] + indices[i:i+1]
#                 cycles[i] = n - i
#             else:
#                 j = cycles[i]
#                 indices[i], indices[-j] = indices[-j], indices[i]
#                 yield "".join(tuple(pool[i] for i in indices[:r]))
#                 break
#         else:
#             return

def verif_word(word: str):
    count = 0
    for c in word:
        if c.isalpha():
            count += 1
    if count == len(word):
        return True
    else:
        return False

def plus_proche(iterable):
    pool = tuple(iterable)
    n = len(pool)
    r = n
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                # print(indices[:r])
                word = "".join(tuple(pool[i] for i in indices[:r]))
                if word > iterable:
                    return word
                break
        else:
            return

valid = False
while not valid:
    try:
        print("Word must be exclusively made of the 26 alphabetic letters")
        word = str(input("Enter word : "))
        if verif_word(word):
            valid = True
    except:
        print("Input error")

print("Permutation la plus proche : ", plus_proche(word))
