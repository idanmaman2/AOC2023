import re 
rules={"red":12,"green":13,"blue":14} 
print(sum(i[0] for i in filter(lambda x :all([all(i <= mx for i,mx in zip(sg, rules.values())) for sg in x[1]]),enumerate(map(lambda x:[[int((re.findall(f"(\d+) {color}",i)+[0])[0]) for color in rules]for i in x.split(";")],open("input_day2.txt",'r').readlines()),1)))) 
