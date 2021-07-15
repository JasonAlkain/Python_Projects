import sqlite3


def newPerson(fname, lname, email):
    return '({},{},{})'.format(fname, lname, email)


conn = sqlite3.connect('.\\Database\\test.db')


with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_persons(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT\
        )')
    conn.commit()
conn.close()


conn = sqlite3.connect('.\\Database\\test.db')
with conn:
    cur = conn.cursor()
    cmd_start = 'INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES(?,?,?)'

    val = ('Bob', 'Smith', 'bsmith@gmail.com')
    cur.execute(cmd_start, val)

    val = ('Sally', 'May', 'smay@gmail.com')
    cur.execute(cmd_start, val)

    val = ('Kevin', 'Bacon', 'kbacon@gmail.com')
    cur.execute(cmd_start, val)

    conn.commit()
conn.close()


conn = sqlite3.connect('.\\Database\\test.db')
with conn:
    cur = conn.cursor()
    cmd_start = 'SELECT col_fname,col_lname,col_email FROM tbl_persons'
    cmd_where = 'WHERE col_fname = "Sally"'
    cur.execute('{} {}'.format(cmd_start, cmd_where))
    var_person = cur.fetchall()
    for item in var_person:
        msg = '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
        msg += 'First Name: {}\n'.format(item[0])
        msg += 'Last Name:{}\n'.format(item[1])
        msg += 'Email: {}\n'.format(item[2])
        msg += '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
        print(msg)
    conn.commit()
conn.close()
