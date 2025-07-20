l= [2,3,5,7,9]
l.append(11)
l.append(13)
l=tuple(l)
print(len(l))
num=int(input("Enter number to check: :"))
if num in l:
    print("Number is in the tuple.")
else:
    print("Number is not in the tuple.")