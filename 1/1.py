file = open("1.txt", "r")
x = 50
count = 0
for line in file:
    l = int(line[1:])
    print(line)
    if line[0] == "R":
        y = x + l
        while y > 99:
            y -= 100
            count +=1
            print("count: ", count)
        x = y
    else:
        y = -l + x
        while y < 0:
            y += 100
            count +=1
            print("count: ", count)
        x = y
    print('so x now', x)
    if x == 0:
        count +=1
        print("landed on 0: count: ", count)
file.close()
print(count, "i")

'''
6792 < ? < 8047

#to pass part 1 should be:
file = open("a.txt", "r")
x = 50
count = 0
for line in file:
    l = int(line[1:])
    if line[0] == "R":
        x = (x + l) % 100
    else:
        x = (100 - l + x) % 100
    print(line, 'so x now', x)
    if x == 0:
        count +=1
file.close()
print(count, "i")

'''
