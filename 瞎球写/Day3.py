#if的用法

#单向判断
stonenumber=6
if stonenumber>=6:
   print('你拥有了毁灭宇宙的力量') 

#双向判断
stonenumber=3
if stonenumber>=6:
    print('你拥有了毁灭宇宙的力量')
    
else:
    print('带着卡魔拉去沃弥尔星寻找灵魂宝石')
    
#多向判断
stonenumber=5

if stonenumber>=6:
    print('你拥有了毁灭宇宙的力量')

elif 0<stonenumber<=5:
    print('绯红女巫需要亲手毁掉幻视额头上的心灵宝石')

else:
    print('需要惊奇队长逆转未来')

#if嵌套
historyscore =26
if historyscore>60:
    print("你已经及格")
    if historyscore>=80:
        print("你很优秀")
    else:
        print("你只是一般般")
else:
    print("不及格")
    if historyscore<=30:
        print("学渣")
    else:
        print("还有抢救的可能")
print("鉴定完毕")

#作业
code = 1
if code>=4:
    print("获得了打败灭霸的力量，反杀稳了")
elif 1<=code<=3:
        print("可以全员出动，殊死一搏")
else:
    print("没办法了，只能尝试呼叫惊奇队长")