st = "AasfjnB#2A22ssf*&BBnnkljjhsjshdj"

hm = {}

for i in st:
    hm[i] = hm.get(i,0) + 1

print(hm)