import re,functools,math
print(math.prod([len([0 for j in range(i+1) if (i-j)*j>d])for i,d in zip(*[map(int,re.findall("\d+",i))for i in open("./inps/input_day6.txt",'r').readlines()])]))