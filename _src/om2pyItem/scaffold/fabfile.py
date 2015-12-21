# _*_ coding:utf-8 _*_


def dataexam():
    import sqlite3
    conn = sqlite3.connect('babyinfo.db')
    cursor = conn.cursor()
    cursor.execute('select * from babyinfo')
    # cursor.execute('select count(*) from babyinfo')
    print cursor.fetchall()
    cursor.close()
    conn.commit()
    conn.close()
