##------------------------Step1---------------------------##
#Step2,3も同じ

#変数定義
natural = 7

#Step4用
natural = int(input("好きな数字を入力してください。"))

if natural < 1:
    print("範囲より小さい数字です。")
elif natural >= 1 and natural < 10:
    print("決められた範囲内の数字です。")
else:
    print("範囲より大きい数字です。")
