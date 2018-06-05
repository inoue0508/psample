'''
正規表現の解答
'''
import re

class Answer_5_3():
    '''
    正規表現の解答
    '''

    

    #定数
    inputFileName = '/home/inoue/python/python.txt'

    ##-------------------------Step1-----------------------------##
    def Step1(self):
        '''
        先頭が多文字で始まる行を表示する。
        '''
        with open(self.inputFileName) as txt:
            for line in txt:
                result = re.match(r'[A-Z].*',line)
                if result:
                    print(result.group())
    
    ##-------------------------Step2-----------------------------##
    def Step2(self):
        '''
        先頭が大文字で始まる行の最初の単語を表示する。
        '''
        with open(self.inputFileName) as txt:
            for line in txt:
                result = re.match(r'[A-Z][^ ]*',line)
                if result:
                    print(result.group())
    
    ##-------------------------Step3-----------------------------##
    def Step3(self):
        '''
        各行の4つ目の単語を表示する。
        '''
        with open(self.inputFileName) as txt:
            for line in txt:
                if line != '\n':
                    print(re.split(r', |,| ',line)[3])
    

    ##-------------------------Step4-----------------------------##
    def Step4(self):
        '''
        cで始まる単語を表示する。
        '''
        with open(self.inputFileName) as txt:
            lines = txt.read()
        print(re.findall(r'\bc\w*\b',lines))