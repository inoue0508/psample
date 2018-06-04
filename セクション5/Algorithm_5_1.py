'''
ファイル操作演習の解答
'''
class Answer_5_1():

    #定数
    txtFileName = '/home/inoue/python/python.txt'
    csvFileName = '/home/inoue/python/python.csv'

    ##-------------------------Step1-----------------------------##
    def Step1(self):
        #ファイル読み込み
        with open(self.txtFileName,'rt') as contents:
            print(contents.read())
    

    ##-------------------------Step2-----------------------------##
    def Step2(self):
        outputFile = '/home/inoue/python/newPython.txt'
        with open(outputFile,'wt') as newFile:
            with open(self.txtFileName,'rt') as contents:
                newFile.write(contents.readline())
    
    ##-------------------------Step3-----------------------------##
    def Step3(self):
        import csv
        with open(self.csvFileName,'r') as contents:
            rows = csv.reader(contents)
            for row in rows:
                print(row)


    ##-------------------------Step4-----------------------------##
    def Step4(self):
        import pandas as pd

        contents = pd.read_csv(filepath_or_buffer=self.csvFileName)
        print(contents)


        

