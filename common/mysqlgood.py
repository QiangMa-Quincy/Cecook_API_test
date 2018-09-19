import  pymysql

conn = pymysql.connect(
    host = '10.12.51.123',
    port = 3306,
    user='scrmuser',
    passwd='cecook2017',
    db ='scrm_sps',
)
try:
    cur = conn.cursor()
    cur.execute("select * from goods_base_info ORDER BY create_time DESC LIMIT 1")
    result = cur.fetchall()

    for row in result:
        lastest_good_name = row[6]
        print(row[6])

except:
    print ("Error: unable to fetch data")
# close mysql
conn.close()