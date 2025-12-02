with open("input.txt") as f:
    lines = [(l[0], int(l[1:])) for l in f.readlines()]

pos = 50
zero_count_p1 = 0
zero_count_p2 = 0

for r, d in lines:
    if r == "L":
        if pos == 0:
            pos = 100
        pos -= d
    else:
        pos += d
    if pos >= 100:
        zero_count_p2 += abs(pos // 100)
    if pos < 0:
        zero_count_p2 += abs(pos // 100)
    if pos == 0:
        zero_count_p2 += 1

    pos %= 100
    if pos < 0:
        pos + 100
        # zero_count_p2 += 1
    if pos == 0:
        zero_count_p1 += 1
        # zero_count_p2 += 1


print(zero_count_p1, zero_count_p2)

# There is bug in my modulo logic, so I go back to the verynaive method while I still can
# (won't be possible in a few days...)


pos = 50
zero_count_p2 = 0
for r, d in lines:
    if r == "R":
        for i in range(d):
            pos += 1
            if pos == 100:
                pos = 0
                zero_count_p2 += 1
    else:
        for i in range(d):
            pos -= 1
            if pos == 0:
                zero_count_p2 += 1
            if pos == -1:
                pos = 99
    # print(f"{r}{d}", pos, zero_count_p2)


print(zero_count_p2)
