valid = False
print("\nDraw Rectangle")
print("--------------\n")

while not valid:
    try:
        print("Width and height must be positive integers")
        w = int(input("Enter width : "))
        h = int(input("Enter height : "))
        if w > 0 and h > 0:
            valid = True
    except:
        print("Input error")

first_line = ["|"] + ["-"] * w + ["|"]
mid_line = ["|"] + [" "] * w + ["|"]

for k in range(h):
    if k == 0 or k == h-1:
        print("".join([k for k in first_line]))
    else:
        print("".join([k for k in mid_line]))
