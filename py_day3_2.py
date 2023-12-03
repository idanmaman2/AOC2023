import itertools,re,string,math,collections
sym=set(string.punctuation)-{'.'}
b=open("./inps/input_dat3.txt",'r').read().strip('\n').split('\n')
gears=collections.defaultdict(list) 
for x in itertools.chain(*[[[i,x]for x in re.finditer("\d+",b[i])]for i in range(len(b))]) : 
    for pc in range(x[1].start(),x[1].end()): 
        for px,py in itertools.product(*[[-1,0,1]]*2): 
            ic,jc=min(max(py+x[0],0),len(b)-1),min(max(px+pc,0),len(b[0])-1)
            if b[ic][jc] == '*' : 
                gears[(ic,jc)].append(int(x[1].group(0)))
                break 
        else: 
            continue 
        break 
print(sum(map(math.prod , filter(lambda x : len(x)==2  , gears.values()))))