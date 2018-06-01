#Stackクラス作成

class Stack():
    
    #配列
    data = list()
    #スタックの頂上
    top = 0

    #メソッド

    #Push
    #スタックに引数で与えられた値を登録します。
    def Push(self,num):
        #最大要素は16
        if len(self.data) <= 16:
            self.data.append(str(num))
        self.top += 1
    
    #Pop
    #スタックに最後に登録した値を取り出します。
    def Pop(self):
        if len(self.data) > 0:            
            temp = self.data.pop(self.top -1)
            self.top -= 1
            return str(temp)
        else:
            return str(-1)

    #ToString
    #Stackに格納されている値をより前に格納した値からカンマ区切りで取り出します。
    def ToString(self):
        if len(self.data) > 0:
            return ",".join(self.data)
        else:
            return "スタックにはもう値がありません。"

