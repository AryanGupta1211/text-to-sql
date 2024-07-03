import mysql.connector as ms

def query_db(sql_query): 
    
    con = ms.connect(host="localhost", user="root", password="root", database="customers")
    cursor = con.cursor()
    cursor.execute(sql_query)
    data = cursor.fetchall()

    cursor.close()
    con.close()
    return data