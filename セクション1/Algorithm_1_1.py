
##---------------------Step1-------------------##

#変数定義
#natural = 99

#if natural < 100:
#    print("100より小さい数字です。")


##---------------------Step2-------------------##

#変数定義
#natural = 111

#if natural < 100:
#    print("100より小さい数字です。")
#else:
#    print("100以上の数字です。")


##---------------------Step3-------------------##

#変数定義米ユーザーからの入力
natural = input("好きな数字を入力してください。")
#naturalは文字列になっているため数値に変換
natural = int(natural)

if natural < 100:
    print("100より小さい数字です。")
else:
    print("100以上の数字です。")
