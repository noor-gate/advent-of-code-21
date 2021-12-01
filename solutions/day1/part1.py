file = open("input.txt", "r");
lines = file.readlines();
depths = list(map(int, lines))
increases = 0

for i in range(len(depths) - 1):
    if depths[i + 1] > depths[i]:
        increases += 1
print(increases)
