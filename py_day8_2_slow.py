import itertools
data = open("./inps/input_day8.txt").read()
path,graph=data.split("\n\n")
path=[{'R':1,'L':0}[i] for i in path]
graph={x[0]:(x[2][1:-1],x[3][:-1]) for x in map(str.split,graph.splitlines())}
next_nodes=filter(lambda x:x[-1]=='A',graph)
for steps,way in enumerate(itertools.cycle(path),1): 
    next_nodes=[graph[next_node][way] for next_node in next_nodes]
    if all(next_node[-1]=='Z' for next_node in next_nodes):
        break
print(steps)
    