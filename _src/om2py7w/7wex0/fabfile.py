# _*_ coding:utf-8 _*_


def dataexam():
    import sqlite3
    conn = sqlite3.connect('noterecord.db')
    cursor = conn.cursor()
    cursor.execute('select * from record')
    print cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
