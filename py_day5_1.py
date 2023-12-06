import re,itertools,functools,bisect
data=open("./inps/input_day5.txt",'r').read()
print(min(functools.reduce(lambda y,x:[i+x[1][bisect.bisect(x[0],i)-1]for i in y],map(lambda x :list(zip(*sorted(x.items(),key=lambda y:y[0]))),map(lambda x:{0:0}|dict((i[1]+i[2],0)for i in x)|dict([i[1],i[0]-i[1]]for i in x),map(lambda x:list(map(lambda x:list(map(int,x[0].split())),re.findall("((\d+\ ?)+)",x))),data.split("\n\n")[1:]))),map(int,re.findall("\d+",data.split("\n")[0])))))
