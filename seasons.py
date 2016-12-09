import os
import re

d = 'C:\\Users\\Alex\\Documents\\glósur\\2.ar\\python\\verk4\\downloads'
r = []
for root, dirs, files in os.walk(d, topdown=False):
    for name in files:
        #o = open(os.path.join(root, name), 'r')
        #l = list(o)
        if re.match(r"s[0-9]+e[0-9]+", name):
            r.append(name)
print(sorted(r)[:10])
