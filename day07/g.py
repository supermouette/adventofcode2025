with open("input.txt") as f:
    lines = [list(l.strip()) for l in f.readlines()]

beams = [(1, lines[0].index("S"))]

visited = set(beams)
split_count = 0
while len(beams) != 0:
    x, y = beams.pop()
    if x == len(lines) - 1:  # beam is at bottom
        continue
    if lines[x][y] == ".":  # beam continue to bottom
        if (x + 1, y) not in visited:
            beams.append((x + 1, y))
            visited.add((x + 1, y))
    if lines[x][y] == "^":  # beam is splitted
        if (x, y + 1) not in visited:
            beams.append((x, y + 1))
            visited.add((x, y + 1))
        if (x, y - 1) not in visited:
            beams.append((x, y - 1))
            visited.add((x, y - 1))
        split_count += 1

print(split_count)
