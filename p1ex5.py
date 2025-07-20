t = input("Enter string: ") 
count = 0
for i in t:
    if i in 'aeiouAEIOU':  
        count += 1
print(count)