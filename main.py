from grades import avg # type: ignore
from rich import print # type: ignore
print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:")
fgl=[]
grade=0
while grade>=0 and grade<=100:
    grade=int(input("Enter a grade for the list (Enter an invalid number to finish): "))
    if grade>=0 and grade<=100:
        fgl.append(grade)
av= avg(fgl)
print(av)

