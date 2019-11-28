a = int(input("第一个数："))
b = int(input("第二个数："))
c = int(input("第三个数："))
if (a>b):
    if (a>c):
        print(a)
    else:
        print(c)
else:
    if (b>c):
        print(b)
    else:
        print(c)
