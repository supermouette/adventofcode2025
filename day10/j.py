import re
import numpy as np
from time import time

with open("input.txt") as f:
    lines = [re.search(r"\[(.*)\](.*)\{(.*)\}", l) for l in f.readlines()]

machines = []

for l in lines:
    lights, buttons, joltage = l.group(1), l.group(2), l.group(3)
    lights = np.array([0 if l == "." else 1 for l in lights])
    buttons = [
        [int(i) for i in b.split(",")]
        for b in buttons[1:-1].replace("(", "").replace(")", "").split(" ")
    ]
    buttons_vec = []
    for b in buttons:
        vec = np.zeros(lights.shape, dtype=np.uint8)
        for light in b:
            vec[b] = 1
        buttons_vec.append(vec)
    joltage = np.array([int(j) for j in joltage.split(",")])
    machines.append([lights, buttons, buttons_vec, joltage])


def get_index(s, e):
    l = []
    for i, c in enumerate(s):
        if c == e:
            l.append(i)
    return l


# part 1
"""
fewest_sum = 0

for lights, buttons, buttons_vec, joltage in machines:
    len_btn = len(buttons_vec)
    working_btn_len = []
    for i in range(2**len_btn):
        bin_i = list(bin(i)[2:].rjust(len_btn, "0"))
        btns = [buttons_vec[idx] for idx in get_index(bin_i, "1")]
        if len(btns) == 0:
            light_status = np.zeros(lights.shape, dtype=np.uint8)
        else:
            light_status = sum(btns) % 2
        if (light_status == lights).all():
            working_btn_len.append(len(btns))
    fewest_sum += min(working_btn_len)

print(fewest_sum)
"""

# part 1
fewest_sum = 0


def get_max_push_btn(btn, joltage):
    idx = []
    for i in range(btn.shape[0]):
        if btn[i] == 1:
            idx.append(i)
    return min([int(joltage[i]) for i in idx])


import pulp
import numpy as np


def solve_min_sum_nonneg_int(M, b):
    # thanks chat GPT
    # well, for this day, there were a few ways :
    # 1 - optimized brut force, probably ~10h run time
    # 2 - write a linear equation solver with free variable
    # 3 - found the exact problem name so that I can use a lib

    k = M.shape[0]

    # Variables (non-negative integers)
    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(k)]

    # Problem
    prob = pulp.LpProblem("min_sum_solution", pulp.LpMinimize)

    # Objective: minimize sum(x)
    prob += pulp.lpSum(x)

    # Constraints: x @ M = b
    for j in range(M.shape[1]):  # columns
        prob += pulp.lpSum(x[i] * M[i, j] for i in range(k)) == b[j]

    # Solve
    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    if pulp.LpStatus[prob.status] != "Optimal":
        return None

    return np.array([xi.value() for xi in x], dtype=int)


for i, (_, buttons, buttons_vec, joltage) in enumerate(machines):
    buttons_mat = np.array(buttons_vec)
    # print(buttons_mat)
    # print(joltage @ np.linalg.pinv(buttons_mat))
    joltage_norm = int(sum(joltage))
    btn_norm = [int(sum(b)) for b in buttons_vec]

    # print("joltage norm", joltage_norm, "btn_norm", btn_norm)

    min_push = max(joltage_norm // max(btn_norm), max(joltage))
    max_push = sum(joltage)
    """
    print(
        "***",
        min_push,
        max_push,
        joltage_norm,
        max(btn_norm),
    )
    """
    max_push_btn = [get_max_push_btn(b, joltage) for b in buttons_vec]
    # print(max_push_btn)
    should_continue = True
    t0 = time()
    # print(f"new_machine: {i}/{len(machines)} ", min_push, max_push)

    x = solve_min_sum_nonneg_int(buttons_mat, joltage)
    # print(x)
    fewest_sum += sum(x)

    # print("loop time", "{:.6f}".format(time() - t0))

print(fewest_sum)
