import collections, string, itertools
map_d = {k: chr(0x40 + v) for v, k in enumerate(string.digits[2:] + "TJQKA", 2)}
print(sum(map(lambda x:(x[0]*int(x[1][1][1])),enumerate(itertools.chain(*[sorted(v,key=lambda x:"".join(map_d[i]for i in x[1][0]))for _, v in itertools.groupby(sorted([("".join(sorted(map(str,collections.Counter(collections.Counter(x[0]).values()).items()),reverse=True)),x)for x in map(str.split,open("./inps/input_day7.txt","r"))],key=lambda x:x[0]),lambda x:x[0])]),1))))


