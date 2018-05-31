##-------------------------Step1、Step2-----------------------------##

#リスト
prime = list()

#一番小さい素数2をリストに格納
prime.append(2)

for n in range(3,101):

    #素数かどうかの判断フラグ
    notSosu = False

    for m in prime:
        if n % m == 0:
            #どれか一つでも割り切れたら素数ではない
            notSosu = True
            break
    
    if notSosu == False:
        prime.append(n)


#以下Step2用の表示成形処理
resultList = list()
for num in range(10,101,10):
    result = ""
    for item in prime:
        if item < num and item >= num - 10:
            result += str(item) + " "
    resultList.append(result)

for item in resultList:
    print(item)
