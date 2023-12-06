import re,functools,math
(x:=list(map(int,re.findall("\d+",open("./inps/input_day6.txt",'r').read().replace(' ','')))),print(len([0 for i in range(x[0])if(x[0]-i)*i>x[1]])))
