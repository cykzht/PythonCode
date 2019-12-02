c = int(input())
d = int(input())
e = int(input())
if(c>d):
    t=c
    c=d
    d=t
elif(c>e):
    t=c
    c=e
    e=t
elif(d>e):
    t=d
    d=e
    e=t
if(c+d<=e):
    print("no")
elif(c**2+d**2==e**2):
    print("zhijiao")
elif(c**2+d**2<e**2):
    print("dunjiao")
elif(c**2+d**2>e**2):
    print("ruijiao")
else:
    print("no")