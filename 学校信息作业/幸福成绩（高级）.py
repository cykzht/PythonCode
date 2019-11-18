a = input("输入三门科目的成绩：")
b = a.split(" ")
c = int(b[0])
d = int(b[1])
e = int(b[2])
f = c>=90
g = d>=90
h = e>=90
if(f==0):
    print(f)
elif(g==0):
    print(g)
elif(h==0):
    print(h)
else:
    h = c%10
    i = d%10
    j = e%10
    if(h==6 or h==8):
        if(i==6 or i==8):
            if(j==6 or j==8):
                print("True")
            else:
                print("False")
        else:
            print("False")
    else:
        print("False")