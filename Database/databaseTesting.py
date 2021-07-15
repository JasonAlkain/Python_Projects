import sqlite3
import os
import sys


# Create a database with a table
# @parameters: dbName tblname
# @defaults: 'test' 'basicTable'
def createTable(dbName='test', tblname='basicTable'):
    conn = sqlite3.connect('.\\Database\\db_{}.db'.format(dbName))
    with conn:
        cur = conn.cursor()
        cmd_start = 'CREATE TABLE IF NOT EXISTS tbl_{}'.format(tblname)
        col_id = 'ID INTEGER PRIMARY KEY AUTOINCREMENT'
        col_file = 'col_file VARCHAR(128)'
        cur.execute('{}({},{})'.format(cmd_start, col_id, col_file))
        conn.commit()
    conn.close()


# add a row to the table inside the database
# @parameters: dbName tblname fname
# @defaults: 'test' 'basicTable' ''
def newRow(dbName='test', tblname='basicTable', fname=''):
    conn = sqlite3.connect('.\\Database\\db_{}.db'.format(dbName))
    with conn:
        cur = conn.cursor()
        cmd_start = 'INSERT INTO tbl_{}(col_file) VALUES(\'{}\')'.format(
            tblname, fname)

        cur.execute(cmd_start)
        conn.commit()
    conn.close()


# get file name from the table inside database
# @parameters: dbName tblname fname
# @defaults: 'test' 'basicTable' ''
def getfName(dbName='test', tblname='basicTable', fname=''):
    conn = sqlite3.connect('.\\Database\\{}.db'.format(dbName))
    with conn:
        cur = conn.cursor()
        cmd_start = 'SELECT * FROM tbl_{}'.format(tblname)

        # is there a file (fname) request
        if fname != '':
            cmd_where = 'WHERE col_file = {}'.format(fname)
            cur.execute('{} {}'.format(cmd_start, cmd_where))
        else:
            cur.execute('{}'.format(cmd_start))

        col_vals = cur.fetchall()
        # pretty display of the information
        for val in col_vals:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            print(val[1])
            #print(openFile(val[1]))
            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        conn.commit()
    conn.close()


# Open a text file and return the data inside
# @parameters: fname
# @defaults: ''
def openFile(fileName=''):
    data = ''
    if fileName != '':
        with open(fileName, 'r') as f:
            data = f.read()
            f.close()
    return data


# add a file to the database
# @parameters: flist ext
# @defaults: ('') '.txt'
def addFile(flist=(''), ext='.txt'):
    # loop through the list
    for file in flist:
        # get file extention
        fileExt = os.path.splitext(file)[1]
        # Check file extention is the same as ext
        if fileExt == ext:
            # if it is then add it to the database
            newRow(dbName='file', tblname='txt_files', fname=file)
            # print the contents of the file
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            print(file)
            #print(openFile(file))
            print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')


if __name__ == "__main__":
    # create a database with the name 'file' with a table named 'txt_files'
    createTable(dbName='file', tblname='txt_files')
    # create a list of tuples with files in it
    fileList = ('information.docx', 'Hello.txt', 'myImage.png',
                'myMovie.mpg', 'Word.txt', 'data.pdf', 'myPhoto.jpg')
    # add a file to the database
    addFile(fileList, '.txt')
