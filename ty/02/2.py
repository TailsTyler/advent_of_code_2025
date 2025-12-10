import csv

with open('1.csv', newline='', encoding='utf-8') as f:
    row = next(csv.reader(f, delimiter=','))
ans = 0
for e in row:
    print('e: ', e)
    i = e.index('-')
    l = e[0:i]
    r = e[i+1:]
    start = True
    while int(l) <= int(r):
        print("l: ", l)
        print("r: ", r)
        length = len(l)
        print("l[0:len(l)//2]: ", l[0:len(l)//2])
        print("l[len(l)//2:]:  ", l[len(l)//2:])
        print("length: ", length)
        i = 1
        potential_repeating_string = l[0]
        while i < len(l)//2:
            while l[i] != l[0]
                potential_repeating_string += l[i]
                i+=1
            while 


        elif not start or l[0:len(l)//2] == l[len(l)//2:]:
            print("found one!: ", l)
            ans+=int(l)
        else:
            first_half = l[0:len(l)//2]
            print("first_half = ", first_half)
            second_half = l[len(l)//2:]
            print("second_half: ", second_half)
            if first_half > second_half:
                l = first_half + first_half
            else:
                first_half = str(int(first_half) + 1)
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
