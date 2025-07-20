l=[1,2,3,4,5]
s=True
for i in range(len(l) - 1):
    if l[i] > l[i+1]:
        s=False
        break
print(s)