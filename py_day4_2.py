import re,functools,operator,itertools
print(sum(len(i)for i in functools.reduce(lambda x,y:x|dict(((y[0],list(itertools.chain('*',*map(lambda z: x[z],y[1])))),)),reversed({i:list(range(i+1,i+j+1))for i,j in enumerate(map(lambda x:len(operator.and_(*(set(re.split("\ +",y))for y in re.match(".+\:\ +(.+)\ +\|\ +(.+)",x).groups()))),open("./inps/input_day4.txt",'r').readlines()),1)}.items()),{'*':'*'}).values())-1)