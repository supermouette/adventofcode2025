with open("input.txt") as f:
    ranges = [[int(i) for i in l.split("-")] for l in f.readlines()[0].split(",")]

print(ranges)


def is_invalid(id):
    sid = str(id)
    lid = len(sid)
    if lid % 2 == 1:
        return False
    else:
        return sid[: lid // 2] == sid[lid // 2 :]


def is_invalid_p2(id):
    sid = str(id)
    lid = len(sid)
    for width in range(1, lid // 2 + 1):
        if lid % width == 0:
            pattern = sid[:width]
            for i in range(lid // width):
                if sid[width * i : width * (i + 1)] != pattern:
                    break
            else:
                return True

    return False


invalid_ids = []
invalid_ids_p2 = []

for start, stop in ranges:
    for id in range(start, stop + 1):
        if is_invalid(id):
            invalid_ids.append(id)
        if is_invalid_p2(id):
            invalid_ids_p2.append(id)

print(sum(invalid_ids))
print(sum(invalid_ids_p2))
