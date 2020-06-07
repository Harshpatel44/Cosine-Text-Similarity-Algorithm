import re
import math
import sys

term_list = sys.argv[1]
file1 = sys.argv[2]
file2 = sys.argv[3]
#opening term_list file and creating a list of words
tl = open(term_list,"r")
term_list=tl.read()
tokens=term_list.split('\n')

#opening file1 and creating a list of words
file1 = open(file1,'r')
file1 = file1.read()
file1=re.sub("[,.!@#$%^&*()~:'<>?/"";`]","",file1)    #eliminating all other special characters
file1=file1.lower()   # eliminating case sensitivity
file1_tokens = file1.split()

#opening file2 and creating a list of words
file2 = open(file2,'r')
file2 = file2.read()
file2=re.sub("[,.!@#$%^&*()~:'<>?/"";`]","",file2)    #eliminating all other special characters
file2=file2.lower()    # eliminating case sensitivity
file2_tokens = file2.split()

#creating 2 dictionaries and assigning all the words from token to 0.
dict_file1={}
dict_file2={}
for i in tokens:
    dict_file1[i]=0
    dict_file2[i]=0

#putting the frequency of the words in the dictionaries
for i in file1_tokens:
    if i in tokens:
            dict_file1[i]+=1
for i in file2_tokens:
    if i in tokens:
        dict_file2[i]+=1
print(dict_file1)
product = sum([a*b for a,b in zip(dict_file1.values(),dict_file2.values())])    # a * b
x_euclidian= math.sqrt(sum([pow(a,2) for a in dict_file1.values()]))            # ||a||
y_euclidian= math.sqrt(sum([pow(b,2) for b in dict_file2.values()]))            # ||b||
try:
    cosine=product / (x_euclidian * y_euclidian)                                    # (a*b)/||a||.||b||
    print(cosine)
except ZeroDivisionError:
    print("Cosine similarity not defined! (Division by zero!)")


