s = []
for x in range(10):
    s.append(int(input()))
print("分數列表式", s)
a = max(s)
b = min(s)
s.remove(a)
s.remove(b)
print("去掉最低分和最高分後的列表是", s)
print("去掉最低分和最高分後選手的平均分是",sum(s)/8)