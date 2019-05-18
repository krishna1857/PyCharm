li = ["Rohit", "Dhawan", "Kohli", "Dhoni", "Pandya", "Rohan", "Dhawal"]
n = len(li)
for i in range(n):
    for j in range(i+1, n):
        if li[i] > li[j]:
            temp = li[i]
            li[i] = li[j]
            li[j] = temp
print li