#input的使用
#input使用
input('请在以下四个选项【格兰芬多；斯莱特林；拉文克劳；赫奇帕奇】中，输入你想去的学院名字:')

#input()函数结果的赋值
name = input('请输入你的选项：')
print(name)

#input()函数的数据类型
choice = input('请输入您的选择：')
if choice == '1':
    print('霍格沃茨欢迎您的到来。')
else:
    print('您可是被梅林选中的孩子，我们不接受这个选项。')

#input()函数结果的强制转换
money = int(input('你一个月工资多少钱？'))

if money >= 10000:
    print('土豪我们做朋友吧！')
elif 5000 < money < 10000:
    print('我们都是搬砖族。。。')
else:
    print('我负责赚钱养家，你负责貌美如花～')

#python爬虫小项目
#数据科学小项目
#web开发小项目
#AI智能小项目

#作业
name = input('你叫什么名字：')
print('哈利·波特的猫头鹰叫做'+name)