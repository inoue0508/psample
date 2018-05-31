##-------------------------Step1-----------------------------##

#2つの数字
# i = 1071
# j = 1029

# while j != 0:
#     if i % j == 0:
#         print(j)
#         break
#     else:
#         temp = j
#         j = i % j
#         i = temp

# if j == 0:
#     print(i)
    

##-------------------------Step1-----------------------------##

i = int(input("自然数入力1："))
j = int(input("自然数入力2(さっきより小さい数)："))

if i < j:
    temp = i
    i = j
    j = temp

while j != 0:
    if i % j == 0:
        print(j)
        break
    else:
        temp = j
        j = i % j
        i = temp

if j == 0:
    print(i)