
import os


def iterateOverFiles(path,index):
    outputNumber = 1
    for filename in os.listdir(path):
        pathBeggining = path + '/'
        fullPath = pathBeggining + filename

        if filename.endswith(".DS_Store") == False:
            readFile1(fullPath,index,str(outputNumber))
            outputNumber += 1

def readFile1(input,index,outputNumber):
    with open(input) as originalFile:
        store = []
        for i in originalFile:
            list = i.strip().split(" ")
            print list[0]

            createFiles(outputNumber,list[index])

def createFiles(number,appendedText):
    with open('/Users/sunilcheema/Documents/pyTestOutput/output' + number + '.txt', "a") as myfile:
        myfile.write(appendedText)


iterateOverFiles('/Users/sunilcheema/Documents/pyTest',1)
