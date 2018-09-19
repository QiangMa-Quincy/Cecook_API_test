import  pymysql

conn = pymysql.connect(
    host = '10.12.51.123',
    port = 3306,
    user='scrmuser',
    passwd='cecook2017',
    db ='cgroup_00002',
)
try:
    cur = conn.cursor()
    cur.execute("select * from member_base_info where cid = 31 ORDER BY create_time DESC LIMIT 1")
    result = cur.fetchall()

    for row in result:
        lastest_member_name = row[44]
        print(row[44])

except:
    print ("Error: unable to fetch data")
# close mysql
conn.close()