#三角形
i = input("请输入三边的长度：")
x = i.split(" ")
a = int(x[0])
b = int(x[1])
c = int(x[2])
q = (a + b + c) / 2
s = (q*(q-a)*(q-b)*(q-c)) ** 0.5
print(s)
