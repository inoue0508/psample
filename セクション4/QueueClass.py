'''
Queueクラス
'''

class Queue():

    #配列
    data = list()

    #次に取り出す要素の位置を示す整数フィールド
    top = 0

    #次に格納する要素の位置を示す整数フィールド
    last = 0

    #Enqueue
    def Enqueue(self,num):
        '''
        キューの末尾に引数で与えられた値を登録する
        '''
        if len(self.data) < 16:
            self.data.append(str(num))
        self.top += 1

    #Dequeue
    def Dequeue(self):
        '''
        キューの先頭データを取得する
        '''
        if len(self.data) > 0:
            return self.data.pop(self.last)
        else:
            return str(-1)
    
    def ToString(self):
        '''
        Queueに格納されている値をカンマ区切りで取り出す。
        '''
        if len(self.data) > 0:
            return ",".join(self.data)
        else:
            return "キューにはもう値がありません。"

    
        
