f = open("day2", "r")

numbers = ["1","2","3","4","5","6","7","8","9","0"]
cubedict = {"red": 12,"green": 13,"blue": 14}
sum = 0
for x in f.readlines():
    igra = x[5:len(x)].split(":")
    igre = igra[1].split(";")
    flag = True
    for cubes in igre:

        cubessplit = cubes.split(",")
        for cube in cubessplit:
            cube = cube.strip().split(" ")
            print(cube)
            if int(cube[0]) > cubedict[cube[1]]:
                flag = False
                break
    if flag:
        sum += int(igra[0])

print(sum)
