##-------------------------Step1,Step2-----------------------------##

#QueueClassの読み込み
import QueueClass

#Queueクラスのインスタンス作成
queIns = QueueClass.Queue()

#取り出した値を入れておくためのリスト
queueList = list()

queIns.Enqueue(1)
queIns.Enqueue(9)
queIns.Enqueue(7)
queueList.append(queIns.Dequeue())
queueList.append(queIns.Dequeue())
queIns.Enqueue(3)
queueList.append(queIns.Dequeue())
queueList.append(queIns.Dequeue())
queueList.append(queIns.Dequeue())

#取り出した値とスタックに残ってる値
print(",".join(queueList))
print(queIns.ToString())