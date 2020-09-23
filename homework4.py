import random
z=[]
for x in range(5):
    a=random.randint(1,100)
    z.append(a)
for x in range(4):
    for y in range(4-x):
        if z[y]<z[y+1]:
            z[y],z[y+1]=z[y+1],z[y]
print("排序後",z)


