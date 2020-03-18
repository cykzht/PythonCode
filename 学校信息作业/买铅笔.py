a = int(input())
b = input()
c = input()
d = input()
e = b.split(" ")
f = c.split(" ")
g = d.split(" ")
b1 = int(e[0])
c1 = int(e[1])
b2 = int(f[0])
c2 = int(f[1])
b3 = int(g[0])
c3 = int(g[1])
if(a%b1==0):
    yi=0
else:
	yi=1
d1=(int(a/b1)+yi)*c1
if(a%b2==0):
	yi=0
else:
    yi=1
d2=(int(a/b2)+yi)*c2
if(a%b3==0):
	yi=0
else:
	yi=1
d3=(int(a/b3)+yi)*c3
if (d1<d2):
    if (d1<d3):
        print(d1)
    else:
        print(d3)
else:
    if (d2<d3):
        print(d2)
    else:
        print(d3)