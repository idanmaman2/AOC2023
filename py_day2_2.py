import re 
colors=("red","green","blue") 
print(sum(i for i in map(lambda x :__import__("functools").reduce(lambda x,y:x*y,(max(vl)for vl in x[1]),1),enumerate(map(lambda x:list(zip(*[[int(re.search(f"(\d+) {color}",i).group(1))if re.search(f"(\d+) {color}",i)else 0 for color in colors]for i in x.split(";")])),open("input_day2.txt",'r').read().split("\n")))))) 