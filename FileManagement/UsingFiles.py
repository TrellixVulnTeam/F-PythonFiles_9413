from io import open

writeFile = open("newTxtFile.txt","w")

writeSentence = "It's a perfect day to learn Python!"

writeFile.write(writeSentence)

writeFile.close()

appendFile = open("newTxtFile.txt","a")

appendSentence= "\nIt's always a good day to code in Python!"

appendFile.write(appendSentence)

appendFile.close()

readFile = open("newTxtFile.txt","r")

readSentence = readFile.read()

readFile.close()

print(readSentence)
