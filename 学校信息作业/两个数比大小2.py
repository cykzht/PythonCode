a = int(input("第一个数："))
b = int(input("第二个数："))
if (a>b):
    t=a
    a=b
    b=t
    print(str(a)+" "+str(b))
else:
    print(str(a)+" "+str(b))
