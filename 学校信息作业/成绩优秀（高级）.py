a = input("输入三门科目的成绩：")
b = a.split(" ")
c = int(b[0])
d = int(b[1])
e = int(b[2])
if(c<d):
    t=c
    c=d
    d=t
elif(c<e):
    t=c
    c=e
    e=t
elif(d<e):
    t=d
    d=e
    e=t
if(c>=90):
    if(d>=90):
        if(e>=90):
            print("3门优秀")
        else:
            print("2门优秀")
    else:
        print("1门优秀")
else:
    print("0门优秀")
