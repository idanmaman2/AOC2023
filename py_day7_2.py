import collections,string,itertools

def create_key(line):
    counted = collections.Counter(line[0])
    prince_count = counted.get('J',0)
    if prince_count: 
        counted.pop('J')
    sorted_counted = sorted(counted.values())
    if sorted_counted : 
        sorted_counted[-1]+=prince_count
    else : 
        sorted_counted=(5,)
    new_hash=collections.Counter(sorted_counted).items()
    return "".join(sorted(map(str,new_hash),reverse=True))

map_d = {k: chr(0x40 + v) for v, k in enumerate('J'+string.digits[2:]+"TQKA", 2)}
data = map(str.split,open("./inps/input_day7.txt","r"))
print(sum(map(lambda x:(x[0]*int(x[1][1][1])),enumerate(itertools.chain(*[sorted(v,key=lambda x:"".join(map_d[i]for i in x[1][0]))for _, v in itertools.groupby(sorted([(create_key(x),x)for x in map(str.split,open("./inps/input_day7.txt","r"))],key=lambda x:x[0]),lambda x:x[0])]),1))))


