s1 = "good morning dear friend "
print "Before Split --> ", s1
word = ''
list1 = []

for i in s1:
    if i == ' ':
        list1.append(word)
        word = ''
    else:
        word = word + i
print "Before Sorting --> ", list1

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
print "After Sorting --> ", list1