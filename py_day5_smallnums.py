import re,itertools,functools
data=open("./inps/input_day5.txt",'r').read()
print(min(functools.reduce(lambda y,x:[x.get(i,i)for i in y],map(lambda x:dict(itertools.chain(*(zip(range(i[1],i[1]+i[2]),range(i[0],i[0]+i[2]))for i in x))),map(lambda x:list(map(lambda x:list(map(int,x[0].split())),re.findall("((\d+\ ?)+)",x))),data.split("\n\n")[1:])),map(int,re.findall("\d+",data.split("\n")[0])))))
