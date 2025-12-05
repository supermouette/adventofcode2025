with open("test.txt") as f:
    lines = f.readlines()

# parsing

ranges = []
ingredients = []
second_part = False
for l in lines:
    if second_part:
        ingredients.append(int(l))
    else:
        if l == "\n":
            second_part = True
        else:
            ranges.append([int(r) for r in l.split("-")])


# part 1
def is_fresh(i):
    for a, b in ranges:
        if i >= a and i <= b:
            return True


fresh_count = 0
for i in ingredients:
    if is_fresh(i):
        fresh_count += 1

print(fresh_count)

# part 2
fresh_count = 0
merged_ranges = []
old_ranges = ""
while old_ranges != str(merged_ranges):
    old_ranges = str(merged_ranges)
    merged_ranges = [ranges[0]]
    for a, b in ranges[1:]:
        for i, (ma, mb) in enumerate(merged_ranges):
            if ma <= a <= mb and ma <= b <= mb:
                break  # range already covered
            elif ma <= a <= mb and b > mb:  # range extended with max
                merged_ranges[i][1] = b
                break
            elif a < ma and ma <= b <= mb:  # range extended with min
                merged_ranges[i][0] = a
                break
        else:
            merged_ranges.append([a, b])
    ranges = merged_ranges.copy()

# print(merged_ranges)

for a, b in merged_ranges:
    fresh_count += b - a + 1

print(fresh_count)  # previous try 346937689802200
