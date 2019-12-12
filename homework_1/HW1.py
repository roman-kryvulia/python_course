
from collections import Counter
import re
from my_module import my_sort

file_name = input("Please input the file name (for example: book): ")+'.txt'
f = open(file_name,"r")

a = dict(Counter(re.findall("\w*",f.read().lower())))

my_sort(a)

f.close()