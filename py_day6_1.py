import math
print(math.prod([len([0 for j in range(i+1)if(i-j)*j>d])for i,d in zip(*map(lambda i:map(int,i.split()[1:]),open("./inps/input_day6.txt",'r')))]))