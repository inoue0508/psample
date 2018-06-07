import re
class Answer_5_4():
    ''' 正規表現：難 の解答 '''

    def Step1(self,ipadr):
        '''ipv6を省略表記に変換する。'''

        #入力されたipv6アドレス
        ipv6 = ipadr

        #最後にコロンを付加するための正規表現
        lastColon = re.compile(r':($)')

        #フィールド毎に先頭の0の並びを削除
        res = re.sub(r'(:|^)0{1,3}',r'\1',ipv6)
        
        i = 8
        while i > 1:
            #連続した:0を探す正規表現
            regex = r'((:|^)0){%d}' % i
            zeroRep = re.compile(regex)

            #（:0）の連続箇所を(：：)に変換
            if zeroRep.search(res) is not None:
                res = zeroRep.sub(r':',res,1)
                res = lastColon.sub(r'::\1',res)
                break

            i -= 1
              
        print(res)
    
    ##-------------------------Step2-----------------------------##
    def Step2(self):
        '''パイソンコメントを削除する。'''

        inputFileName = "/home/inoue/python/commentdelete.py"
        outputFileName = "/home/inoue/python/output.py"

        with open(inputFileName) as txt:
            contents = txt.read()
        
        #[''']か["""]に囲まれたコメント削除
        regex = re.compile(r'("|\'){3}([^\'"]|\n)*(\1){3}')
        result = regex.sub('',contents)

        # #のコメント削除
        result = re.sub(r'( |\t)*#.*\n','',result)

        #ファイルに結果を出力
        with open(outputFileName,'wt') as txt:
            txt.write(result)
        print(result)

