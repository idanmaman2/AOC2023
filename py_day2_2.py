import math
colors=("red","green","blue") 
print(sum(map(lambda x:math.prod((max(vl)for vl in x[1])),enumerate(map(lambda x:list(zip(*[({c:0 for c in colors}|dict((x.split()[1],int(x.split()[0])) for x in i[1:].split(", "))).values()for i in x[x.find(": ")+1:].split(";")])),open("input_day2.txt",'r').readlines()))))) 