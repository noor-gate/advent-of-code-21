file = open("input.txt", "r");
lines = file.readlines();
depths = list(map(int, lines))
windows = []
increases = 0

for i in range(len(depths) - 2):
    windows.append(depths[i + 2] + depths[i + 1] + depths[i])

for i in range(len(windows) - 1):
    if windows[i + 1] > windows[i]:
        increases += 1
print(increases)
