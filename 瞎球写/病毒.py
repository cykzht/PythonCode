from turtle import *
pensize(5)
i=0
while True:
    pencolor("purple")
    fd(-20)
    right(90)
    circle(-10,340)
    left(60)
    fd(22)
    left(90)
    pencolor("green")
    circle(-250,10)
    right(90)
    i+=1
    if(i==18):
        break
done()
