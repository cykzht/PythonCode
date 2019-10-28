a = input('请输入一个三位数：')   #等待输入
b = int(a) / 100   #百位数提取
c = int(a) % 100 /10   #十位数提取
d = int(a) % 100 % 10   #各位数提取
e = int(b)   #百位整数化
f = int(c)   #十位整数化
g = int(d)   #个位整数化
print(str(d) + str(c) + str(b))
