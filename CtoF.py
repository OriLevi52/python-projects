def ToF(x):
    return x*(9/5)+32
def ToC(x):
    return(x-32)*5/9
v= int(input("Choose to what would you like to convert (1 to Farenheit, 2 to Celsius): "))
if v==1:
    J=int(input("How many in celsius? "))
    J=ToF(J)
    print(J)
elif v==2:
    J=int(input("How many in farenheit? "))
    J=ToC(J)
    print(J)
else:
    print("Undefined choice.")