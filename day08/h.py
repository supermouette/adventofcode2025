is_test = False
if is_test:
    filename = "test.txt"
    nb_pair = 10
else:
    filename = "input.txt"
    nb_pair = 1000

with open(filename) as f:
    boxes = [[int(c) for c in l.split(",")] for l in f.readlines()]

distances = []
for i in range(len(boxes)):
    xi, yi, zi = boxes[i]
    for j in range(i + 1, len(boxes)):
        xj, yj, zj = boxes[j]
        distances.append(
            (
                ((xj - xi) ** 2 + (yj - yi) ** 2 + (zj - zi) ** 2) ** 0.5,
                (i, j),
            )
        )

distances.sort(key=lambda x: x[0])

circuits: list[set] = []

for d, (bi, bj) in distances[:nb_pair]:
    # identify if bi and bj are already in a circuit
    ci, cj = None, None
    for cii, c in enumerate(circuits):
        if ci is None and bi in c:
            ci = cii
        if cj is None and bj in c:
            cj = cii
        if ci is not None and cj is not None:
            break

    if ci is None and cj is None:  # create a new circuit
        circuits.append(set((bi, bj)))
        # print("create new circuits", bi, bj, boxes[bi], boxes[bj])
    elif ci is None and cj is not None:
        circuits[cj].add(bi)
        # print("adding to a circuit", bi)
    elif ci is not None and cj is None:
        circuits[ci].add(bj)
        # print("adding to a circuit", bj)
    elif ci != cj:  # merge circuits
        # print("merge 2 circuits")
        to_remove = max(ci, cj)
        circuits[min(ci, cj)] = circuits[ci] | circuits[cj]
        del circuits[max(ci, cj)]
    else:  # circuits already merged, do nothing
        # print("do nothing !")
        pass
    # print("----", circuits)


circuits.sort(key=lambda x: -len(x))
# print(circuits)
print(len(circuits[0]), len(circuits[1]), len(circuits[2]))

print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))
