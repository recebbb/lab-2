import random, math
n=20
massiv=[]
cem=0
for i in range(n):
    massiv.append(random.randint(0,50))

for k in massiv:
    cem+=k
sin=math.sin(cem)
print(sin)