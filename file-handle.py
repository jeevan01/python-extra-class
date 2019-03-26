def writetext(mytext, filename):
    fp = open(filename, "w")
    fp.write(mytext)
    fp.close()

def readtext(filename):
    fp = open(filename, "r")
    text = fp.read()
    print("read file : ", text)
    fp.close()

filekonaam = str(input("Where do you wanna save ? : "))
writetext(input("Enter what you wanna save ? :"),filekonaam)
readtext(filekonaam)

# ask the user to which file do you wanna save the text?