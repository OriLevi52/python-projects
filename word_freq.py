import sys
def reading(file_path):
    with open(file_path) as file: #opening the file
        d ={} #creating a dictionary to save the words and times of occurances in
        for line in file:
            splitted=line.split() #splitting between words and times
            for word in splitted:
                if word in d:
                    d[word]+=1#adding to the current value
                else:
                    d[word]=1#creating new value if there isn't
        return d
    
def sorting(dictionary,n):
  l=sorted(dictionary.items(),key=lambda item: item[1], reverse=True) #sorting the dictionary by times of apperance for each word (lowest to highest)   
  l=l[:n]
  sorted_d=dict(l)
  return sorted_d

n=int(input("Enter number:"))#(top n words)
path="C://Users//Ori Levi//Downloads//python projects//pt5.txt"#reffering to the txt file we want to sort
d=reading(path)
d=sorting(d,n)
for key, value in d.items():
    print("The word '"+key+"' appears "+str(value)+" times")