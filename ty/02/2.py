import csv

with open('t.csv', newline='', encoding='utf-8') as f:
    row = next(csv.reader(f, delimiter=','))


def all_9s(s):
    for e in s:
        if e != '9':
            return False
    return True

'''
finds appropriate start for when a new level of magnituede is reached eg
10 -> 1 1
100 -> 1 1 1
1000 -> 10 10
10000 -> 1 1 1 1 1
100000 -> 100 100
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
            print('\tstarter_for_this_num_of_digits made ans ', ans)
            return ans, rs
        i+=1
          
        


#used only when the current id is invalid
def next_invalid_id(l, prs):
    #if prs is all 9s, just increase l by 1
    if all_9s(l):
        print("all 9s")
        #add one to make eg 999 become 1000
        l = str(int(l) + 1)
        print("starter_for_this_num_of_digits")
        return starter_for_this_num_of_digits(l)
    #otherwise increase rs by 1
    else:
        l2 = l
        prs = str(int(prs) + 1)
        i = 0
        l2 = ''
        while i < len(l) // len(prs):
            l2 += prs
            i+=1
        if l2 == '':
            #if there is no prs, we want to stop looking by making l larger than r
            l2 = str(int(r) + 1)
        print('returning an l2 of', l2, "and a prs of ", prs)
        return l2, prs
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
def first_invalid_id(l):
    if int(l) < 11:
        return '11', '1'
    '''
    consider the large l of 
    11885 11880
    the first invalid is
    11885 11885.
    In other words, divide the fewest times possible and paste the leftmost part
    '''
    cut = 2
    while cut <= len(l):
        #if the cut fits without a remainder,
        if len(l) % cut == 0:
            #create a possible answer
            prs = l[0:len(l) // cut]
            ans = prs * cut
            #and if it is not less than the current l, return it
            if ans >= l:
                print("first_invalid_id returning ", ans, "&", prs)
                return ans, prs
        cut += 1
    '''even cut into single digets, the answer did not work. for example,
    e:  1698522-1698528
        1111111
        is too small.
        so make it
        2222222
    '''
    prs = str(int(prs) + 1)
    print("got an overflow situation")
    if prs == "10": #TODO 100 prs could fail
        print('got here')
        return starter_for_this_num_of_digits(str(len(ans) + 1))
    print('in a 1111111-type situation')
    return prs * cut, prs



def process_row(e, row, ans):
    print("ans was3: ", ans, "\n")
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
            l, prs = first_invalid_id(l)
            known_invalid = True
        if known_invalid:
            print("ans was: ", ans, "\n")
            print("ans += ", l)
            ans += int(l)
            print("ans: ", ans, "\n")
        #increase l to next possible invalid id
        print("getting next invalid id")
        l, prs = next_invalid_id(l, prs)  
       
        limit += 1
        if limit > 2:
            print('\t limit reached!')
            break
    print("ans was1: ", ans, "\n")
    return ans

def process_rows(row):
    ans = 0
    for e in row:
        print("ans was before process: ", ans, "\n")
        ans += process_row(e, row, ans)
        print("ans was after process: ", ans, "\n")
    return(ans)

# def tests():
    # print("all_9s('1')",  all_9s('1'))
    # print("all_9s('19')",  all_9s('19'))
    # print("all_9s('999')",  all_9s('999'))
    # print("next_invalid_id('12', '1'): ", next_invalid_id('12', '1'))
    # print("starter_for_this_num_of_digits(10): ", starter_for_this_num_of_digits('10'))
    # print("starter_for_this_num_of_digits(100): ", starter_for_this_num_of_digits('100'))
    # print("starter_for_this_num_of_digits(1000): ", starter_for_this_num_of_digits('1000'))
    # print("starter_for_this_num_of_digits(10000): ", starter_for_this_num_of_digits('10000'))
    # print("starter_for_this_num_of_digits(100000): ", starter_for_this_num_of_digits('100000'))
    #if

#tests()
#correct answer for first 4: 1188514137
first_4 = ['11-22', '95-115','998-1012','1188511880-1188511890']
debugging_mystery_23_added_to_ans = ['11-22','95-115', '1010-1011']
print(process_rows(debugging_mystery_23_added_to_ans))
#print(process_rows(row))


'''

4102072058 you before
4196610578 you now
79532879456
4174379265 correct


    

'''

