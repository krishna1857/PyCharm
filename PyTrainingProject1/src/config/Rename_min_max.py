s = "I work for Money"
sl = s.split()
l_len = [len(i) for i in sl]

print(sl, l_len)
data = {}
for i in sl:
    data[len(i)] = i
print(data)

smin = l_len[0]
smax = l_len[0]
for i in l_len:
    if smax < i : smax = i
    if smin > i : smin = i
    else: pass
print("smin, smax",smin, smax)

for p,i in enumerate(l_len):
    if i == smin: l_len[p] = smax
    if i == smax: l_len[p] = smin
print("Replaced index -> ",l_len)

fList = []
for i in l_len:
    for j in data.keys():
        if i == j:
            fList.append(data[j])
print(fList)