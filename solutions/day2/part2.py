file = open("input.txt", "r");
lines = file.readlines();
horizontal = 0
depth = 0
aim = 0

for line in lines:
    instr, num = line.split()
    num = int(num)
    if instr == "forward":
        horizontal += num
        depth += aim * num
    elif instr == "down":
        aim += num
    else:
        aim -= num
print(depth * horizontal)

