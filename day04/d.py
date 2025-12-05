with open("input.txt") as f:
    lines = [[c for c in l.strip()] for l in f.readlines()]

width = len(lines)  # square map

dirs = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

movable_rolls = 0
for i in range(width):
    for j in range(width):
        if lines[i][j] == ".":
            continue
        adj = 0
        for di, dj in dirs:
            x, y = i + di, j + dj
            if x < 0 or y < 0 or x == width or y == width:
                continue
            if lines[x][y] == "@":
                adj += 1
        if adj < 4:
            movable_rolls += 1
print(movable_rolls)  # p1


total_rolls = 0
stop = False
while not stop:
    movable_rolls = []
    for i in range(width):
        for j in range(width):
            if lines[i][j] == ".":
                continue
            adj = 0
            for di, dj in dirs:
                x, y = i + di, j + dj
                if x < 0 or y < 0 or x == width or y == width:
                    continue
                if lines[x][y] == "@":
                    adj += 1
            if adj < 4:
                movable_rolls.append((i, j))
    # print(movable_rolls)
    if len(movable_rolls) == 0:
        stop = True
    else:
        total_rolls += len(movable_rolls)
        for x, y in movable_rolls:
            lines[x][y] = "."
print(total_rolls)  # p2
