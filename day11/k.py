with open("input.txt") as f:
    lines = [l.strip().split(": ") for l in f.readlines()]

devices = {}

for device, output in lines:
    o = output.split(" ")
    devices[device] = o

to_visit = [["you"]]
complete_path = []

while len(to_visit) != 0:
    path = to_visit.pop()
    for output in devices[path[-1]]:
        new_path = path[:] + [output]
        if output == "out":
            complete_path.append(new_path)
        elif output not in path:
            to_visit.append(new_path)


print(len(complete_path))
