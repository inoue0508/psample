##-------------------------Step3-----------------------------##

#行列の大きさ決定
print("行列の大きさを入力してください。")
brow = int(input("かけかれる行列の行："))
bcolumn = int(input("かけかれる行列の列："))
arow = bcolumn
print("かける行列の行：{0}".format(arow))
acolumn = int(input("かける行列の列："))

multipliedMatrix = [[0 for i in range(bcolumn)] for j in range(brow)]
multiplyMatrix = [[0 for i in range(acolumn)] for j in range(arow)]
resultMatrix = [[0 for i in range(acolumn)] for j in range(brow)]

#行列の値の入力
print("かけられる行列の値を入力してください")
a = 0
while a < brow:
    b = 0
    while b < bcolumn:
        multipliedMatrix[a][b] = int(input("かけられる行列{0}行{1}列：".format(a+1,b+1)))
        b += 1
    a += 1

print("かける行列の値を入力してください")
a = 0
while a < arow:
    b = 0
    while b < acolumn:
        multiplyMatrix[a][b] = int(input("かけられる行列{0}行{1}列：".format(a+1,b+1)))
        b += 1
    a += 1

#行列の計算
m = 0
while m < brow:
    n = 0
    while n < acolumn:
        l = 0
        while l < bcolumn:
            resultMatrix[m][n] += multipliedMatrix[m][l] * multiplyMatrix[l][n]
            l += 1
        n += 1
    m += 1

#結果表示
for itemList in resultMatrix:
    for item in itemList:
        print(item,end="")
        print(" ",end="")
    print("")
