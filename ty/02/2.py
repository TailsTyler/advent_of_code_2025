import csv

with open('m.csv', newline='', encoding='utf-8') as f:
    row = next(csv.reader(f, delimiter=','))


def all_9s(prs):
    for e in prs:
        if e != '9':
            return False
    return True


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
        print("l[0:len(l)//2]: ", l[0:len(l)//2])
        print("l[len(l)//2:]:  ", l[len(l)//2:])
        i = 1
        #potential_repeating_string
        prs = l[0]
        print("len(l)//2: ", len(l)//2)
        while i <= len(l)//2:
            print("i = ", i)
            '''
            must ignore prs that l is not divisible by:
            with
            221111,
            221 221
            must be found before
            22 22 22
            hence
            'or len(l) % i not 0'
            '''
            while l[i] != l[0] or len(l) % i != 0:
                prs += l[i]
                i+=1
            
            #todo
            valid = False
            #compare prs to rest of l
            while i< len(l):
                for j in prs:
                    if l[i] != j:
                        valid = True
                        print("break 1")
                        l+=1
                        break
                break
            if not valid:
                print("ans += ", l)
                ans += int(l)
                print("ans: ", ans)
            #increase l to next possible invalid id
            #if prs is all 9s, just increase l by 1
            if all_9s(prs):
                l = str(int(l) + 1)
            #otherwise increase rs by 1
            prs = str(int(prs) + 1)
            i = 0
            new_l = ''
            while i < len(l) / len(prs):
                new_l+= prs
        break
       
        '''
        11 -22
        111 - 222
        1212 1313

        21 21
        2 2 2 2 
        23 23 

        12 12
        13 13 

        12 22
        1211 1212
        121120 
        999
        9999

        99 99







            
            
            
            
                




        # elif not start or l[0:len(l)//2] == l[len(l)//2:]:
        #     print("found one!: ", l)
        #     ans+=int(l)
        # else:
        #     first_half = l[0:len(l)//2]
        #     print("first_half = ", first_half)
        #     second_half = l[len(l)//2:]
        #     print("second_half: ", second_half)
        #     if first_half > second_half:
        #         l = first_half + first_half
        #     else:
        #         first_half = str(int(first_half) + 1)
        #         l = first_half + first_half
        #     print("l = ", l)
        #     start = False
        #     continue    
        # #jumps ahead to next match 
        # l = l[0:len(l)//2] #cut off 2nd half 
        # l = str(int(l) + 1) #increment
        # l += l # dupe 1st half to make 2nd half
        # print('l increased to ', l)
        # start = False
        





    

'''

