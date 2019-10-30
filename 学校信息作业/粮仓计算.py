#粮仓
n = int(input("请输入5月1日粮食的量;"))
wuer = n + 20
wusan = wuer * (1 / 3)
ws = int(wusan)
wusi = wusan * 2 + wusan
wss = int(wusi)
print(str(n) + " " + str(wuer) + " " + str(ws) + " " + str(wss))
