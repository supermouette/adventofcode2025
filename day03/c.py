with open("input.txt") as f:
    lines = [[int(c) for c in list(l.strip())] for l in f.readlines()]


joltage = 0
joltage_2 = 0
for bank in lines:
    first_digit = max(bank[:-1])
    i = bank[:-1].index(first_digit)
    second_digit = max(bank[i + 1 :])
    joltage += 10 * first_digit + second_digit

    digits = []
    last_i = 0
    nb_left = bank[:]
    for d in range(12):
        numbers_left = 12 - d
        max_i = len(bank) - numbers_left + 1
        if len(digits) == 0:
            digit = max(bank[:max_i])
            last_i = bank[:max_i].index(digit)
        else:
            digit = max(bank[last_i + 1 : max_i])
            last_i = last_i + 1 + bank[last_i + 1 : max_i].index(digit)
        digits = [digit] + digits
    joltage_2 += int("".join([str(d) for d in digits[::-1]]))


print(joltage)
print(joltage_2)
