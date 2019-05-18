import copy
d = [4, 2, 5, 8, 1, 1]       #,11,72,822,3,9]
a = copy.copy(d)
n = len(d)

for i in range(1, n):  #Loop from 1 to last element
    hole = i
    while(hole > 0  and d[hole-1] > d[hole]):
        value = d[hole]
        d[hole] = d[hole-1]
        d[hole - 1] = value
        hole = hole -1

print a, d


'''
li = [4, 2, 5, 8, 1, 1]
n = len(li)
for i in range(n):
    for j in range(i+1, n):
        if li[i] > li[j]:
            temp = li[i]
            li[i] = li[j]
            li[j] = temp
print li

'''

