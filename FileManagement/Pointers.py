readFile = open("newTxtFile.txt", "r")

readSentence = readFile.read()

print(readSentence)

print("\nThe text  printed will start on the 11th position\n")

readFile.seek(11)

readSentence = readFile.read()

print(readSentence)

print("\nThe text  printed is the string formed by the first 11 characters of the text\n")#COMMENT WHAT IS BEFORE THIS EXCEPT LINE 1

readSentence = readFile.read(11)

print(readSentence)

readFile.close()
