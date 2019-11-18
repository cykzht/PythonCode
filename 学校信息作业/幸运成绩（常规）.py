#成绩是否幸运，逻辑运算
a = input("输入三门科目的成绩：")
b = a.split(" ")
c = int(b[0])
d = int(b[1])
e = int(b[2])
f = c>=90
g = d>=90
h = e>=90
i = c-96==0 or c-98==0
j = d-96==0 or d-98==0
k = e-96==0 or e-98==0
h = f+g+h+i+j+k==6
print(h)