import numpy as np

a = np.random.randint(1, 100, size=(10,2))
d = dict(a)
print(len(d))
print(str(d))
d2 = dict()

#for k, v in d.items():
#    d2[v] = k
#    print(len(d2))
#    print(str(d2))

#d.update(d2)
#print(len(d))
#print(str(d))
 
for k, v in list(d.items()):
    d[v] = k
    print(len(d))
    print(str(d))

