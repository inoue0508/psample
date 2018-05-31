##-------------------------Step1-----------------------------##

#変数定義※ユーザー入力
n = int(input("好きな数字を入力してください。"))

if n % 15 == 0:
    print("BuzzFizz")
elif n % 5 == 0:
    print("Buzz")
elif n % 3 == 0:
    print("Fizz")
else:
    print(n)