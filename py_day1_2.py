import re 
import string 
digits = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine') 
ddigits = dict(zip(digits + tuple(string.digits[1:])  , string.digits[1:]*2 ))
first_num  = lambda x : re.search("|".join(digits) + "|[1-9]" ,x).group(0)
last_num =  lambda x : re.search(".*(" + "|".join(digits) + "|[1-9]).*?$" ,x).group(1)
print(sum(map(lambda x:int(ddigits[first_num(x)]+ddigits[last_num(x)]),open("./input.txt" ,'r').readlines())))

