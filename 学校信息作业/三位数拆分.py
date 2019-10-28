#三位数提取
a = input('请输入一个三位数：')
x = int(a)
if 100<=x<1000:
    b = x / 100   #百位数提取
    c = x %100 /10   #十位数提取
    d = x %100 % 10   #各位数提取
    e = int(b)
    f = int(c)
    g = int(d)
    print('百位数为：' + str(e))
    print('十位数为：' + str(f))
    print('个位数为：' + str(g))
else:
    print('你输入的好像不是三位数')
