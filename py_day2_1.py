rules={"red":12,"green":13,"blue":14} 
print(sum(i[0] for i in filter(lambda x :all([all(i <= mx for i,mx in zip(sg, rules.values())) for sg in x[1]]),enumerate(map(lambda x:[({c:0 for c in rules}|dict((x.split()[1],int(x.split()[0])) for x in i[1:].split(", "))).values()for i in  x[x.find(": ")+1:].split(";")],open("./inps/input_day2.txt",'r').readlines()),1)))) 