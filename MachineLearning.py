# Advay Koranne
# Machine Learning Project
# September 14 2019


# DataStructure: dictionary

# play tennis,outlook,temperature,humidity,wind ( each one of these are the keys)
# no,sunny,hot,high,weak (one day) - one entry in the linked list [0]  contains dictioaaries where the key is the atribute


# in node class store children as dictionaries the keys for these dictionaries could be the values of the atribute, the values of the map would be node that is your child
import math
myfile = open("TennisDataSet.txt","r")
training_set = []
texting_set = []

days = {} # dictionary which will store the atribute as the key and the and the value as the result


header = myfile.readline().strip().split(',')
category = header[0:] # depdent
#print("category" , category)
#print("")
first_line = header[0:] # end is default # attributes( indepdent)
print("atributes" , first_line)
#days['new key'] = 'new value'




header = myfile.readline().strip().split(',')
#print("header", header)
attributes = header[1:] # depdent


header = myfile.readline().strip().split(',')
#category = header[0:] # depdent
#print("category" , category)
def ReadFile(file):
    lines = []
    for line in open(file):
        sentence = line.strip().split(",")
        print("")
        dict = {}
        for item in first_line:
            for word in sentence:
                print(" " , word)
            #dict.append(word:sentence)
            #dict[word] = sentence
            #print (word)

        lines.append(dict)


            #attributes = header[1:] # end is default # attributes( indepdent)

            #print(attributes)

        #for word in sentence:
            #print(word.split(","))

        #items = line.split(',')
        #list.append(items)
        #print(list[0])
        #print(items)
        #list.append(line)
        #print(list[0])
print(list)
ReadFile("TennisDataSet.txt")
print(dict)

def entropy(Yes,No):
    entropy = -(Yes)*(math.log(Yes)/math.log(2)) - (No) * (math.log(No)/math.log(2))
    print (entropy)

Yes = 5
No = 10

entropy(Yes,No)
