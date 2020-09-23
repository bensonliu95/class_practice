num_list=[]
for x in range(100):
    x += 1
    num_list.append(x)
print(num_list)
for i in num_list:
    if i%2 == 1:
        num_list.remove(i)
print(num_list)
