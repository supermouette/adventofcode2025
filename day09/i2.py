with open("input.txt") as f:
    tiles = [[int(t) for t in l.strip().split(",")] for l in f.readlines()]

# p1
areas = []

for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        x1, y1 = tiles[i]
        x2, y2 = tiles[j]
        areas.append((abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))
print(max(areas))

# p2

green_tiles = set()

for i in range(len(tiles)):
    x1, y1 = tiles[i]
    x2, y2 = tiles[(i + 1 if i + 1 != len(tiles) else 0)]
    if y1 == y2:
        for j in range(min(x1, x2), max(x1, x2) + 1):
            green_tiles.add((j, y1))
    else:
        for j in range(min(y1, y2), max(y1, y2) + 1):
            green_tiles.add((x1, j))

"""
for i in range(13):
    s = []
    for j in range(9):
        if (i, j) == (3, 4):
            s.append("o")
        else:
            s.append("#" if (i, j) in green_tiles else ".")
    print("".join(s))
"""

areas = []

xs = [x for x, y in tiles]
min_x = min(xs) - 1
max_x = max(xs) + 1
# ys = [y for x, y in tiles]
# min_y = min(ys) - 1
# max_y = max(ys) + 1

inner_tiles = set()


def is_in_polygon(x, y):
    # extra fast check
    if (x, y) in green_tiles:
        return True
    # check if there is an immediate neighbor which is inside inner_tiles
    if (x - 1, y) in inner_tiles or (x + 1, y) in inner_tiles:
        inner_tiles.add((x, y))
        return True
    # is x closer to min_x or max_x ?
    if x - min_x < max_x - x:
        r = (min_x, x + 1)
    else:
        r = (x, max_x + 1)
    was_tile = False
    count = 0
    for i in range(r[0], r[1]):
        if was_tile:
            if (i, y) not in green_tiles:
                count += 1
                was_tile = False
        else:
            if (i, y) in green_tiles:
                was_tile = True
        # print(i, y, (i, y) in green_tiles, was_tile, count)
    if count % 2 == 1:
        inner_tiles.add((x, y))
        return True
    return False


for i in range(len(tiles)):
    print("starting row", i)
    inner_tiles = set()  # clear cache, I'm afraid of ram usage
    for j in range(i + 1, len(tiles)):
        x1, y1 = tiles[i]
        x2, y2 = tiles[j]
        # fast check: only continue if four squares are in green tiles
        if not is_in_polygon(x1, y2) or not is_in_polygon(x2, y1):
            continue
        # slow check : only if every side are in green tiles (will this be enough ???)
        should_stop = False
        for k in range(min(x1, x2), max(x1, x2) + 1):
            if not is_in_polygon(k, y1) or not is_in_polygon(k, y2):
                should_stop = True
                break
        if should_stop:
            continue
        for k in range(min(y1, y2), max(y1, y2) + 1):
            if not is_in_polygon(x1, k) or not is_in_polygon(x2, k):
                should_stop = True
                break
        if should_stop:
            continue
        # print((x1, y1), (x2, y2), (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))
        areas.append((abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))
print(max(areas))
