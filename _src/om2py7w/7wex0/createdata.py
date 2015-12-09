# _*_ coding:utf-8 _*_
# It's no need.

import sqlite3

def main():
    conn = sqlite3.connect('noterecord.db')
    cursor = conn.cursor()
    cursor.execute('create table record (time text, record varchar)')
    cursor.execute("insert into record (time, record) values ('2015-12-07 00:01:00', 'test')")
    cursor.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()