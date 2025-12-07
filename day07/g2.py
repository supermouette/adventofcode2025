from functools import lru_cache

with open("input.txt") as f:
    lines = [list(l.strip()) for l in f.readlines()]


@lru_cache(maxsize=10**6)
def count_timelines(x, y):
    if x == len(lines) - 1:  # beam is at bottom
        return 1
    if lines[x][y] == ".":  # beam continue to bottom
        return count_timelines(x + 1, y)
    if lines[x][y] == "^":  # beam is splitted
        return count_timelines(x, y + 1) + count_timelines(x, y - 1)


print(count_timelines(1, lines[0].index("S")))
