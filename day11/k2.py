from functools import lru_cache


with open("input.txt") as f:
    lines = [l.strip().split(": ") for l in f.readlines()]

devices = {}

for device, output in lines:
    o = output.split(" ")
    devices[device] = o


@lru_cache(maxsize=10**6)
def count_path(start, stop):
    if start == stop:
        return 1
    next = devices.get(start, [])
    count = 0
    count = sum([count_path(d, stop) for d in next])
    return count


@lru_cache(maxsize=10**6)
def count_path_stop(start, stop, is_dac, is_fft):
    if start == stop and is_dac and is_fft:
        return 1
    if start == "dac":
        is_dac = True
    if start == "fft":
        is_fft = True
    next = devices.get(start, [])
    count = 0
    count = sum([count_path_stop(d, stop, is_dac, is_fft) for d in next])
    return count


print(count_path("you", "out"))  # p1
print(count_path("svr", "out"))
print(count_path_stop("svr", "out", False, False))  # p2
