##-------------------------Step1,Step2-----------------------------##

#Stack.py読み込み
import StackClass

#Stackクラスのインスタンス化
stackIns = StackClass.Stack()

#取り出した値を入れておくためのリスト
popList = list()

stackIns.Push(1)
stackIns.Push(9)
stackIns.Push(7)
popList.append(stackIns.Pop())
stackIns.Push(3)
popList.append(stackIns.Pop())
popList.append(stackIns.Pop())

#Step2用に追加
popList.append(stackIns.Pop())
popList.append(stackIns.Pop())

#取り出した値とスタックに残ってる値
print(",".join(popList))
print(stackIns.ToString())

