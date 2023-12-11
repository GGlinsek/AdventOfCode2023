f = open("day2", "r")

numbers = ["1","2","3","4","5","6","7","8","9","0"]

sum = 0
for x in f.readlines():
    igra = x[5:len(x)].split(":")
    igre = igra[1].split(";")
    cubedict = {"red": 0, "green": 0, "blue": 0}
    for cubes in igre:

        cubessplit = cubes.split(",")
        for cube in cubessplit:
            cube = cube.strip().split(" ")
            print(cube)
            if int(cube[0]) > cubedict[cube[1]]:
                cubedict[cube[1]] = int(cube[0])

    sum += cubedict["red"]*cubedict["blue"]*cubedict["green"]

print(sum)
