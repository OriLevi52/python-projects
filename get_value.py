def get_value(dictionary, key):
    t = False
    for i in dictionary.keys():
        if key == i:
            t = True
            return(dictionary[i]) 
    if not t:
        return("Error")
my_dict = {"apple": 5, "banana": 8, "orange": 12}
print(get_value(my_dict,"apple"))
print(get_value(my_dict,"pineapple"))
