#温度输出
val = input("请输入温度表示符号的温度值（例如：32C）:")
if val[-1] in ['C','c']:
    f = 1.8 * float(val[0:-1]) + 32
    print("转换后的温度：%.2fF"%f)
elif val[-1] in ['F','f']