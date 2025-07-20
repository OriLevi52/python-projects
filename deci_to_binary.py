Dnum = int(input("Enter decimal number: "))
Bnum = 0
digit_mover=1
while Dnum >0:
    Bnum += int((Dnum%2)*digit_mover)
    Dnum= int(Dnum/2)
    digit_mover*=10
print(Bnum)