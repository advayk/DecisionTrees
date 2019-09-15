# Advay Koranne
# Machine Learning Project
# September 14 2019


import math

file = list()
def ReadFile(file):
    lines = open(file).read()
    #list = []
    #list.append(lines)
    print(lines)
    #for var in list:
        #print(list.index(var), var)

ReadFile("TennisDataSet.txt")


def entropy(Yes,No):
    entropy = -(Yes)*(math.log(Yes)/math.log(2)) - (No) * (math.log(No)/math.log(2))
    print (entropy)

Yes = 5
No = 10

entropy(Yes,No)
