##-------------------------Step1、Step2-----------------------------##

#100個の要素を持つリスト生成
naturals = [1]  * 100

for i in range(2,11):
    if naturals[i] == 0:
        continue
    j = i + 1
    while j < 100:
        if j % i == 0:
            naturals[j] = 0
        j += 1

#Step2用の表示結果整形処理
num = 2
beforNum = 0
while num < 100:  
    if naturals[num] == 1:
        if str(beforNum).zfill(2)[:1] == str(num).zfill(2)[:1]:
            print(" ",end="")
            print(num,end="")
        else:
            print("")
            print(num,end="")
        beforNum = num
    num += 1
print("")
