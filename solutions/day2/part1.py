file = open("input.txt", "r");
lines = file.readlines();
horizontal = 0
depth = 0

for line in lines:
    instr, num = line.split()
    num = int(num)
    if instr == "forward":
        horizontal += num
    elif instr == "down":
        depth += num
    else:
        depth -= num
print(depth * horizontal)

