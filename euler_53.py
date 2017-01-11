from __future__ import division
import itertools

lengths = {}
for i in range(23,101):
    x = i/2
    y = 2
    r = []
    while len(list(itertools.combinations(range(1,i+1),y))) < 1000000:
        y+=1
        r.append(y)
    lengths.update({i:max(r)})
    print(max(r))

summer = 0
for key, value in lengths.items():
    k = key
    v = value
    print(len(range(v,(k+1)-v)))
    summer += len(range(v,(k+1)-v))
