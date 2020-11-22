import mysql.connector

if __name__ == '__main__':
    conn = mysql.connector.connect(host='localhost', user='root', password='123456', database='test')

    cursor = conn.cursor()

    cursor.execute('select * from student')
    values = cursor.fetchall()
    print(values)

    cursor.execute('select * from student where id=%s', ('1',))
    value = cursor.fetchone()
    print(value)

    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
    print(cursor.rowcount)
    conn.commit()
    cursor.close()
    conn.close()

