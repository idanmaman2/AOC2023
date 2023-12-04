import operator,math
print(sum(map(lambda x:math.floor(2**(len(operator.and_(*(set(y.split())for y in x.split("|"))))-1)),open("./inps/input_day4.txt",'r').readlines())))