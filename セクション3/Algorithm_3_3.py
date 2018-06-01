##-------------------------Step1、Step2-----------------------------##

#3x3の配列
#かけられ得る行列
#(1,1,1)
#(1,1,1)
#(1,1,1)
multpliedMatrix = [[1 for i in range(3)] for j in range(3)]

#Step2のユーザー入力用
#かけられる行列（かける行列も同じように）
i = 0
while i < 3:
    j = 0
    while j < 3:
        multpliedMatrix[i][j] = int(input("かけられる行列{0}行{1}列目：".format(i,j)))
        j += 1
    i += 1


#かける行列
#(1,2,3)
#(1,2,3)
#(1,2,3)
multplyMatrix = [[i for i in range(1,4)] for j in range(1,4)]

#結果行列
resultMatrix = [[0 for i in range(3)] for j in range(3)]

#かけ算
a = 0
while a < 3:
    b = 0
    while b < 3:
        resultMatrix[a][b] = multpliedMatrix[a][0] * multplyMatrix[0][b] + multpliedMatrix[a][1] * multplyMatrix[1][b] + multpliedMatrix[a][2] * multplyMatrix[2][b]
        b += 1
    a += 1

#結果表示
for itemList in resultMatrix:
    for item in itemList:
        print(item,end="")
        print(" ",end="")
    print("")

