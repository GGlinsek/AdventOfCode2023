f = open("day1-1","r")

numbers = ["1","2","3","4","5","6","7","8","9","0"]

sum = 0
for x in f.readlines():
    linenumbers = []
    for s in x:
        if s in numbers:
            linenumbers.append(int(s))
    sum += linenumbers[0] *10 + linenumbers[-1]


print(sum)

