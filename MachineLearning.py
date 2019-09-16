# Advay Koranne
# Machine Learning Project
# September 14 2019


# DataStructure: dictionary

# play tennis,outlook,temperature,humidity,wind ( each one of these are the keys)
# no,sunny,hot,high,weak (one day) - one entry in the linked list [0]  contains dictioaaries where the key is the atribute



import math
myfile = open("TennisDataSet.txt","r")
list = []
training_set = []
texting_set = []

header = myfile.readline().strip().split(',')
categroy = header[0] # depdent
attributes = header[1:] # end is default # attributes( indepdent)

print("---", header,"---")
print("")
print(attributes)

def ReadFile(file):
    for line in open(file):
        list.append(line)
        line = line.strip()
        items = line.split(',')
        print(line)

    print(list[0])


ReadFile("TennisDataSet.txt")


def entropy(Yes,No):
    entropy = -(Yes)*(math.log(Yes)/math.log(2)) - (No) * (math.log(No)/math.log(2))
    print (entropy)

Yes = 5
No = 10

entropy(Yes,No)
