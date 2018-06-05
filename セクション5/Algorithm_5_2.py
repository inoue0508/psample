'''
ファイル操作演習の解答
'''

class Answer_5_2():
    #定数
    inputFileName = '/home/inoue/python/python.txt'

    ##-------------------------Step1-----------------------------##
    def Step1(self):
        '''
        先頭から16文字を表示
        '''
        with open(self.inputFileName,'rt') as txt:
            contents = txt.read()
        print(contents[:16])
    
    ##-------------------------Step2-----------------------------##
    def Step2(self):
        '''
        文字数を表示する
        '''
        with open(self.inputFileName,'rt') as txt:
            contents = txt.readlines()
        for line in contents:
            print("{0}文字：{1}".format(len(line),line))
    

    ##-------------------------Step3-----------------------------##
    def Step3(self):
        '''
        文字数を表示する。スペース、改行を除く。
        '''
        with open(self.inputFileName,'rt') as txt:
            contents = txt.readlines()
        for line in contents:
            print("{0}文字：{1}".format(len(line.replace(" ","").replace("\n","")),line))

    ##-------------------------Step4-----------------------------##
    def Step4(self):
        '''
        1行目の2番目の単語を表示
        '''
        with open(self.inputFileName,'rt') as txt:
            contents = txt.readline()
            print(contents.split()[1])
    
    ##-------------------------Step5-----------------------------##
    def Step5(self):
        '''
        2行目の各単語の先頭を大文字にする。
        '''
        with open(self.inputFileName,'rt') as txt:
            txt.readline()
            contents = txt.readline()
            print(contents.title())
    
    ##-------------------------Step6-----------------------------##
    def Step6(self):
        '''
        [a]という単語を2つ含む行を表示する。
        '''
        with open(self.inputFileName,'rt') as txt:
            for line in txt:
                if line.split().count('a') == 2:
                    print(line)
    