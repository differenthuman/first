dict = {}
origin = open("hydro.txt","r");
p = origin.readline().split()
for a in origin.readlines():
    for b in a.split():
        dict[b] = dict.get(b, 0)+1
sdict = sorted(dict.items(), key = lambda kv : kv[1], reverse=True)
print(sdict)
