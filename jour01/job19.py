n_start = 1
n_end = 100
fizz = 3
buzz = 5

for k in range(n_start, n_end+1):
    if k%(fizz*buzz) == 0:
        print("FizzBuzz")
    elif k%fizz == 0:
        print("Fizz")
    elif k%5 == 0:
        print("Buzz")
    else:
        print(k)
