import psycopg2

class ConnectPostgresql():
    '''ポスグレに接続してみる'''

    #コネクション情報
    connection = None

    #コンストラクタ
    def __init__(self):
        '''
        コンストラクタ
        DBに接続する
        '''
        ipAddress = "10.0.2.15"
        port = "5432"
        dbName = "sample"
        userName = "inoue"
        password = "****"

        self.connection = psycopg2.connect("host={0} port={1} dbname={2} user={3} password={4}"
                                        .format(ipAddress,port,dbName,userName,password))

    def Select(self):
        '''selectする'''

        cur = self.connection.cursor()
        cur.execute("select id,name from sampletable")

        for row in cur:
            print(row[0],row[1])
    
