import csv

with open('1.csv', newline='', encoding='utf-8') as f:
    row = next(csv.reader(f, delimiter=','))
ans = 0
for e in row:
    print('e: ', e)
    print("ans: ", ans)

'''

'''
