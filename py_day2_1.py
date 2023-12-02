import re 
rules={"red":12,"green":13,"blue":14} 
print(sum(i[0] for i in filter(lambda x :all([all(i <= mx for i,mx in zip(sg, rules.values())) for sg in x[1]]),enumerate(map(lambda x:[[int(re.search(f"(\d+) {color}",i).group(1))if re.search(f"(\d+) {color}" ,i )else 0 for color in rules]for i in x.split(";")],open("input_day2.txt",'r').read().split("\n")),1)))) 
