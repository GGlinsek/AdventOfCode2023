f = open("day1-2", "r")

numbers = ["1","2","3","4","5","6","7","8","9","0"]
wordnumbers = ["one","two","three","four","five","six","seven","eight","nine","zero"]

sum = 0
lines = []
for x in f.readlines():
    line = ""
    substringline = ""
    t = x
    for i in range(5, len(x)):

        m = t[i-5:i].replace("one", "1")
        t = t[0:i-5] + m + t[i:len(t)]

        t = t.replace("two", "2")

        t = t.replace("three", "3")

        t = t.replace("four", "4")

        t = t.replace("five", "5")

        t = t.replace("six", "6")

        t = t.replace("seven", "7")

        t = t.replace("eight", "8")

        t = t.replace("nine", "9")

        t = t.replace("zero", "0")
        line+=t[0]
        substringline = x[i-4:i]
    line += substringline
    print()
    lines.append(line)

for x in lines:
    linenumbers = []
    for s in x:
        if s in numbers:
            linenumbers.append(int(s))
    sum += linenumbers[0] *10 + linenumbers[-1]



print(sum)

