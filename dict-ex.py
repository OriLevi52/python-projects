dicti={"John" : 90, "Jay" : 80, "Jonah" : 85, "James" : 70}
dicti["Jordan"]=100
dicti["James"]=72
e=0
c=0
for i in dicti.values():
    e+=i
    c+=1
sum=float(e/c)
print(sum)
del dicti["Jonah"]
check=str(input("Enter name of student: "))
print(check in dicti)
