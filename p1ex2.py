def even(l):
    new_list=[]
    for i in l:
        if i%2==0:
            new_list.append(i)
    print(new_list)
original_list=[1,4,5,7,8,10,13]
even(original_list)