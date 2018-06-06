import pandas as pd

class Answer_5_5():
    '''
    csvファイル集計の問題の解答クラス
    '''

    #ファイルのパス
    inputFilePath = '/home/inoue/python/python.csv'

    ##-------------------------------Step1--------------------------------##
    def Step1(self):
        '''
        先頭から2行を表示する。
        '''
        data = pd.read_csv(self.inputFilePath)
        print(data.head(2))
    
    ##-------------------------------Step2--------------------------------##
    def Step2(self):
        '''
        5,6列目を表示する。
        '''
        data = pd.read_csv(self.inputFilePath)
        print(data.iloc[:,4:6])

    ##-------------------------------Step3--------------------------------##
    def Step3(self):
        '''
        高さが1.0以上の行を表示する。
        '''
        data = pd.read_csv(self.inputFilePath)
        print(data.query("高さ >= 1.0"))
    
    ##-------------------------------Step4--------------------------------##
    def Step4(self):
        '''
        重い順に並び変える
        '''
        data = pd.read_csv(self.inputFilePath)
        print(data.sort_values(by=["重さ"],ascending=False))

    ##-------------------------------Step5--------------------------------##
    def Step5(self):
        '''
        高さ、重さの最大値、最小値、平均を求める。
        '''
        data = pd.read_csv(self.inputFilePath)
        hmax = data["高さ"].max()
        hmin = data["高さ"].min()
        have = data["高さ"].mean()

        hmaxName = data.query("高さ == @hmax")["名前"].values[0]
        hminName = data.query("高さ == @hmin")["名前"].values[0]

        wmax = data["重さ"].max()
        wmin = data["重さ"].min()
        wave = round(data["重さ"].mean(),1)

        wmaxName = data.query("重さ == @wmax")["名前"].values[0]
        wminName = data.query("重さ == @wmin")["名前"].values[0]
        
        print("高さ最大：{0}：{1}m".format(hmaxName,hmax))
        print("高さ最小：{0}：{1}m".format(hminName,hmin))
        print("高さ平均：{0}m".format(have))
        print("重さ最大：{0}：{1}kg".format(wmaxName,wmax))
        print("重さ最小：{0}：{1}kg".format(wminName,wmin))
        print("重さ平均：{0}kg".format(wave))

    ##-------------------------------Step6--------------------------------##
    def Step6(self):
        '''タイプ1毎に高さと重さの平均を求める。'''

        data = pd.read_csv(self.inputFilePath)
        groupData = data.groupby("タイプ1")
        have = round(groupData["高さ"].mean(),1)
        wave = round(groupData["重さ"].mean(),1)

        resultData = pd.DataFrame(columns=["タイプ1","高さ平均","重さ平均"])
        resultData["タイプ1"] = have.index
        resultData["高さ平均"] = have.values
        resultData["重さ平均"] = wave.values
        print(resultData)


      

    ##-------------------------------Step7--------------------------------##
    def Step7(self):
        '''
        BMIを計算新たな列を追加する
        '''
        data = pd.read_csv(self.inputFilePath)

        #BMIリスト
        bmiList = list()
        for index,row in data.iterrows():
            bmiList.append(round(row.values[5] / (row.values[4] ** 2),1))
        
        data["BMI"] = bmiList
        print(data)