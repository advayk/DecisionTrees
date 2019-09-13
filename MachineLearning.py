
def ReadFile(file):
    text_file = open(file, "r")
    lines = text_file.readlines()
    print (lines, sep = ",")

ReadFile("TennisDataSet.txt")
