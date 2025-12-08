import csv

with open('t.csv', newline='', encoding='utf-8') as f:
    row = next(csv.reader(f, delimiter=','))
ans = 0
for e in row:
    print('e: ', e)
    i = e.index('-')
    l = e[0:i]
    print('l: ', l)
    r = e[i+1:]
    print('r: ', r)
    start = True
    while int(l) <= int(r):
        length = len(l)
        print("l[0:len(l)//2]: ", l[0:len(l)//2])
        print("l[len(l)//2:]:  ", l[len(l)//2:])
        print("length: ", length)
        print("length % 2: ", length % 2)
        if length % 2: #odd num of digits so cannot be something repeated twice
            #always start w something like 11, 1010, 100100, etc
            #make first half by adding howevermany 0s
            l = '1' + ('0' * (length // 2)) 
            l+= l #add duped second half
            print("new l: ", l)
            continue
        elif not start or l[0:len(l)//2] == l[len(l)//2:]:
            print("found one!: ", l)
            ans+=int(l)
        else:
            first_half = l[0:len(l)//2]
            print("first_half = ", first_half)
            l = first_half + first_half
            print("l = ", l)
            start = False
            continue
        #jumps ahead to next match
        l = l[0:len(l)//2] #cut off 2nd half 
        l = str(int(l) + 1) #increment
        l += l # dupe 1st half to make 2nd half
        print('l increased to ', l)
        start = False
        

    print("ans: ", ans)



    

'''


'''
