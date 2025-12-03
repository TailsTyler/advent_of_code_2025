file = open("a.txt", "r")
x = 50
count = 0
for line in file:
    l = int(line[1:])
    if line[0] == "R":
        y = x + l
        while y > 99:
            y -= 100
            count +=1
        x = y
    else:
        y = -l + x
        while y < 0:
            y += 100
            count +=1
        x = y
    print(line, 'so x now', x)
    if x == 0:
        count +=1
file.close()
print(count, "i")

'''
6792 < ? < 8047
'''
