import itertools,re,string
b=open("./inps/input_dat3.txt",'r').read().strip('\n').split('\n')
print(sum(int(nm[1].group(0))for nm in filter(lambda x:any(b[min(max(py+x[0],0),len(b)-1)][min(max(px+pc,0),len(b[0])-1)]not in string.digits+'.'for pc in range(x[1].start(),x[1].end())for px,py in itertools.product(*[[-1,0,1]]*2)),itertools.chain(*[[[i,x]for x in re.finditer("\d+",b[i])]for i in range(len(b))]))))