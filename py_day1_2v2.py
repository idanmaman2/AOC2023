import re 
import string 
digits = ('one','two','three','four','five','six','seven','eight','nine') 
ddigits = dict(zip(digits+tuple(string.digits[1:]),string.digits[1:]*2))
print(sum(map(lambda x:int(ddigits[re.search("|".join(digits) + "|[1-9]" ,x).group(0)]+ddigits[ re.search("|".join(i[::-1] for i in digits) + "|[1-9]" ,x[::-1]).group(0)[::-1]]),open("./input.txt" ,'r').readlines())))

