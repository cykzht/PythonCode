#成绩是否优秀，逻辑运算
a = input("输入三门科目的成绩：")
b = a.split(" ")
c = int(b[0])
d = int(b[1])
e = int(b[2])
f = c>=90
g = d>=90
h = e>=90
i = int(f) + int(g) + int(h)
print(str(i)+"门优秀")