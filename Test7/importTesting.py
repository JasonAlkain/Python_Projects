import os


def writeData(fileName='', data='', openMode='a'):
    data = data  # 'Hello, world'
    with open(fileName, openMode) as f:
        data = f.write(data)
        f.close()


def openFile(fileName=''):
    if fileName != '':
        with open(fileName, 'r') as f:
            data = f.read()
            print('\n\n')
            print(data)
            print('\n\n')
            f.close()


if __name__ == "__main__":
    testFile = './test.txt'
    wd = '\I love Python'
    writeData(testFile, wd, 'w')
    openFile(testFile)


# writeData('./test.txt', 'Hello world')
# openFile('./test.txt')
