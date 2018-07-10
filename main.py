import os


def iterateOverFiles(path,index):
    outputNumber = 1
    for filename in os.listdir(path):
        pathBeggining = path + '/'
        fullPath = pathBeggining + filename
        if filename.endswith(".DS_Store") == False:
            readFile(fullPath,index,str(outputNumber))
            outputNumber += 1


def readFile(input,index,outputNumber):
    with open(input) as originalFile:
        store = []
        for i in originalFile:
            list = i.strip().split(" ")
            createFiles(outputNumber,list[index])


def createFiles(number,appendedText):
    with open('/Users/sunilcheema/Documents/pyTestOutput/output' + number + '.txt', "a") as myfile:
        myfile.write(appendedText)
    with open('/Users/sunilcheema/Documents/pyTestOutput/outputAll.txt', "a") as myfile2:
        myfile2.write(' ' + appendedText)


iterateOverFiles('/Users/sunilcheema/Documents/pyTest',1)
