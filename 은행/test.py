import pymysql
import datetime
import pandas as pd


create = "INSERT INTO 고객정보 (계좌번호, 계좌형태, 예금주, 생년월일, 비밀번호, 잔액) VALUES (%s,%s,%s,%s,%s,%s)"
create_sa = "INSERT INTO 고객정보 (계좌번호, 계좌형태, 예금주, 생년월일, 비밀번호, 잔액, 만기해지일) VALUES (%s,%s,%s,%s,%s,%s,%s)"
in_out_create = "INSERT INTO 입출금통장 (계좌번호, 예금주, 입금액, 잔액) VALUES (%s,%s,%s,%s)"
saving_create = "INSERT INTO 적금통장 (계좌번호, 예금주, 입금액, 잔액, 만기일) VALUES (%s,%s,%s,%s,%s)"
#in_deposit = 
#out_deposit = "INSERT INTO 입출금통장 (account, name, withdraw, balance) VALUES (%s,%s,%s,%s,%s)"
db = 'banksysdb'

conn = pymysql.connect(host= 'localhost', port=3306, user = 'camel3118',
                        password = 'Pbldb1234',
                        db = 'banksysdb',
                        charset = 'utf8')


def deposit_in(account, balance):

    sql = "SELECT 계좌번호, 예금주, 잔액 FROM 입출금통장 WHERE 계좌번호=%s ORDER BY 거래일 DESC LIMIT 1"
    sql_in = "INSERT INTO 입출금통장 (계좌번호, 예금주, 입금액, 보낸분_받는분, 잔액) VALUES(%s,%s,%s,%s,%s)" 
    data1 = []
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, (account))
            result = cur.fetchall()
            for data in result:
                data1 = data1 + list(data)
            print(data1, type(data1))
            sum1 = int(data1[2])+int(balance)
            print(sum1)
            cur.execute(sql_in, (account, data1[1], balance, data1[1], sum1))
            conn.commit()
            
    

            

deposit_in(3333, 50000)