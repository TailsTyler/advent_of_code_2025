import csv

with open('m.csv', newline='', encoding='utf-8') as f:
    row = next(csv.reader(f, delimiter=','))


def all_9s(s):
    for e in s:
        if e != '9':
            return False
    return True

'''
finds appropriate start for when a new level of magnituede is reached eg
10 -> 11
100 -> 111
1000 -> 1010
10000 -> 11111
100000 -> 100100
'''
def starter_for_this_num_of_digits(l):
    if len(l) == 2:
        return '11', '1'
    i = 2
    while i <= len(l):
        if len(l) % i == 0:
            rs = '1'
            rs_len = len(l) // i
            for x in range(rs_len - 1):
                rs += '0'
            
            ans = rs
            for x in range(i - 1):
                ans += rs
            return ans, rs
        i+=1
          
        


#used only when the current id is invalid
def next_invalid_id(l, prs):
    print("l3: ", l)
    if not known_invalid:
        return get_prs(l)
    #if prs is all 9s, just increase l by 1
    if all_9s(l):
        print("all 9s")
        #add one to make eg 999 become 1000
        l = str(int(l) + 1)
        return starter_for_this_num_of_digits(l)
    #otherwise increase rs by 1
    else:
        l2 = l
        print("prs: ", prs)
        print("prs = str(int(prs) + 1)")
        prs = str(int(prs) + 1)
        print("prs: ", prs)
        i = 0
        l2 = ''
        print('l: ', l)
        print("finding any next rs")
        print("len(l): ", len(l))
        print("len(prs): ", len(prs))
        print("len(l) // len(prs): ", len(l) // len(prs))
        while i < len(l) // len(prs):
            print("l2 = ", l2)
            print("l2 += prs")
            l2 += prs
            i+=1
            print("l2 = ", l2)
        if l2 == '':
            #if there is no prs, we want to stop looking by making l larger than r
            l2 = str(int(r) + 1)
        return l2
def get_prs(l):
    #potential_repeating_string
    prs = l[0]
    print("len(l)//2: ", len(l)//2)
    # print("i <= len(l)//2")
    # print(i <= len(l)//2)

    i = 1
    while i < len(l)//2 and l[i] != l[0] or len(l) % i != 0:
        print("l: ", l)
        print("i = ", i)
        '''
        get prs

        must ignore prs that l is not divisible by:
        with
        221111,
        221 221
        must be found before
        22 22 22
        hence
        'or len(l) % i not 0'
        '''
        prs += l[i]
        i+=1
    return prs

#gets the first invalid id above the current valid one
def first_invalid_id(l, prs):
    ans = prs
    while len(ans) < len(l):
        ans+= prs
    if len(ans) != len(l):
        print("first_invalid_id failed")
    return ans

def tests():
    print("all_9s('1')",  all_9s('1'))
    print("all_9s('19')",  all_9s('19'))
    print("all_9s('999')",  all_9s('999'))
    print("next_invalid_id('12', '1'): ", next_invalid_id('12', '1'))
    print("starter_for_this_num_of_digits(10): ", starter_for_this_num_of_digits('10'))
    print("starter_for_this_num_of_digits(100): ", starter_for_this_num_of_digits('100'))
    print("starter_for_this_num_of_digits(1000): ", starter_for_this_num_of_digits('1000'))
    print("starter_for_this_num_of_digits(10000): ", starter_for_this_num_of_digits('10000'))
    print("starter_for_this_num_of_digits(100000): ", starter_for_this_num_of_digits('100000'))

#tests()
ans = 0
for e in row:
    print('e: ', e)
    i = e.index('-')
    l = e[0:i]
    r = e[i+1:]
    known_invalid = False
    limit = 0
    while int(l) <= int(r):
        print("l: ", l)
        print("r: ", r)
        # print("l[0:len(l)//2]: ", l[0:len(l)//2])
        # print("l[len(l)//2:]:  ", l[len(l)//2:])
        if not known_invalid:
            i = 1
            #potential_repeating_string
            prs = get_prs(l)
            #compare prs to rest of l
            while i< len(l):
                for j in prs:
                    if l[i] != j:
                        print("break 1")
                        break
                break
            #we have a valid string, so make it the next possible invalid one by pasting the prs until it fills l. So like with '95', we start w '' and paste 9s until we have '99'
            l = first_invalid_id(l, prs)
            known_invalid = True
        if known_invalid:
            print("ans += ", l)
            ans += int(l)
            print("ans: ", ans, "\n")
        #increase l to next possible invalid id
        print("ll1: ", l)
        print("prs: ", prs)
        print("getting next invalid id")
        l, prs = next_invalid_id(l, prs)  
        print("ll: ", l)
        limit += 1
        if limit > 2:
            print('\t limit reached!')
            break
print("ans: ", ans)
        
       
'''

m
11-22,95-115, 112-112


too low

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

