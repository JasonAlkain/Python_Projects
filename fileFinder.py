import time
import os
import hashlib


def writeData(fileName='', data='', openMode='a'):
    data = data  # 'Hello, world'
    with open(fileName, openMode) as f:
        data = f.write(data)
        f.close()


def openFile(fileName=''):
    data = ''
    if fileName != '':
        with open(fileName, 'r') as f:
            data = f.read()
            f.close()
    return data


def getPath(dirName):
    path = os.getcwd()
    return os.path.join(path, dirName)


def findFiles(path):
    dirs = os.listdir(path)
    for file in dirs:
        fileExt = os.path.splitext(file)[1]
        if fileExt == '.txt':
            filePath = getPath('{}\\{}'.format(path, file))
            modTime = os.path.getmtime(filePath)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('Last modification time:\n\t {}\n'.format(time.ctime(modTime)))
            print('File: \n\t{}\n'.format(file))
            print(openFile(filePath))
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        else:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('Not a txt file and can not be read at the time.')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    pass


def makeRNDFiles(fileCount=10, lineCount=5, folder=''):
    from random import randint
    for i in range(fileCount):
        path = getPath('{}\\file_{}.txt'.format(folder, i))
        hashStr = ''
        for i in range(lineCount):
            rndStr = str(randint(0, 10)).encode('utf-8')
            hashStr += '{}\n'.format(hashlib.sha256(rndStr).hexdigest())
        writeData(path, hashStr, 'w')


if __name__ == "__main__":
    # I made this because I was lazy...
    # uncomment for fun!
    #makeRNDFiles(lineCount=3, folder='FileReading')

    # Finds and prints files with the extention '.txt'
    findFiles(getPath('FileReading'))
    pass
