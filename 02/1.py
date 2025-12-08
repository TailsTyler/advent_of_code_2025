import csv

with open('t.csv', newline='', encoding='utf-8') as f:
    row = next(csv.reader(f, delimiter=','))
for e in row:
    print(e)
    i = e.index('-')
    l = e[0:i]
    print(l)
    r = e[i+1:]
    print(r)
    while int(l) <= int(r):
        length = len(l)
        if length % 2: #odd num of digits so cannot be something repeated twice
            new_l = '1' #always start w something like 11, 1010, 100100, etc
            l = '1' + ('0' * (length // 2)) #make first half
            l+= l #add duped second half
            print("new l: ", l)
        


    

'''


'''
