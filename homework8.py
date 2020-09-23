import random
a=random.randint(1,100)
b=random.randint(1,100)
c=random.randint(1,100)
Chinese=a
print(Chinese)
Math=b
print(Math)
English=c
print(English)
D=Chinese+Math+English
print(D)
if D>=270:
    print("優秀")
elif D<270 and  D>=240:
    print("良好")
elif D<240 and  D>=180:
    print("合格")
else:
    print("不合格")