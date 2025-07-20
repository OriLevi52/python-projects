def find_palindromes(l):
    nl=[]
    for i in l:
        if i == i[::-1]:
            nl.append(i)
    return nl
l= ['moon','noon','wow','hi']
print(find_palindromes(l))