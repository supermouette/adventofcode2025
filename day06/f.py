from functools import reduce

with open("input.txt") as f:
    lines = [[nb for nb in l.strip("\n").split(" ") if nb != ""] for l in f.readlines()]

grand_total = 0
for i in range(len(lines[0])):
    nbs = []
    for j in range(len(lines) - 1):
        nbs.append(lines[j][i])
    if lines[-1][i] == "*":
        grand_total += reduce(lambda x, y: int(x) * int(y), nbs, 1)
    else:
        grand_total += sum([int(nb) for nb in nbs])

print(grand_total)

with open("input.txt") as f:
    lines = [l.strip("\n") for l in f.readlines()]


ops = []

for i in range(len(lines[-1])):
    if lines[-1][i] != " ":
        ops.append((i, lines[-1][i]))

ops.append((len(lines[-1]) + 1, ""))

grand_total = 0
for i in range(len(ops) - 1):
    op = ops[i][1]
    a, b = ops[i][0], ops[i + 1][0] - 1
    extract = [l[a:b] for l in lines[:-1]]
    nbs = []
    for j in range(len(extract[0])):
        nb = "".join([c[j] for c in extract])
        if nb.startswith(" "):
            nb.replace(" ", "0")
        nbs.append(int(nb))

    if op == "*":
        grand_total += reduce(lambda x, y: int(x) * int(y), nbs, 1)
    else:
        grand_total += sum([int(nb) for nb in nbs])
print(grand_total)
