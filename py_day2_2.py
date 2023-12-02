import re,math
colors=("red","green","blue") 
print(sum(i for i in map(lambda x:math.prod((max(vl)for vl in x[1])),enumerate(map(lambda x:list(zip(*[[int((re.findall(f"(\d+) {color}",i)+[0])[0]) for color in colors]for i in x.split(";")])),open("input_day2.txt",'r').read().split("\n")))))) 