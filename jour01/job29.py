valid = False
print("\nDraw Triangle")
print("--------------\n")

while not valid:
    try:
        print("Height must be a positive integer")
        h = int(input("Enter height : "))
        w = h
        if h > 0:
            valid = True
    except:
        print("Input error")

last_line = ["/"] + ["-"] * (w-1)*2 + ["\\"]

for k in range(h):
    if k == h-1:
        print("".join([k for k in last_line]))
    else:
        mid_line = [" "] * (w-k-1) + ["/"] + [" "] * k*2 + ["\\"]
        print("".join([k for k in mid_line]))
