print(sum(map(lambda x:int(next(filter(str.isdigit,x))+next(filter(str.isdigit,reversed(x)))),open("./input.txt",'r').readlines()))) 