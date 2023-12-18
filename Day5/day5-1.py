f = open("day5", "r")

seeds = f.readline().strip().split(":")[1].strip().split()
print(seeds)
counter = 0
for line in f.readlines():
    if line == "\n":
        counter += 1
    elif counter == 1:
        counter -= 1
    else:
        numbers = line.strip().split()
        for i in range(0, len(seeds)):
            if int(numbers[1]) < int(seeds[i]) < int(numbers[1]) + int(numbers[2]):
                seeds[i] = int(seeds[i]) - int(numbers[1]) + int(numbers[2])