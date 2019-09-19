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
first_line = header[1:] # end is default # attributes( indepdent)

print(len(category))

header = myfile.readline().strip().split(',')
attributes = header[1:] # depdent


header = myfile.readline().strip().split(',')


lines = []

def ReadFile(file):
    for line in open(file):
        sentence = line.strip().split(",")
        dict = {}
        for word, attribute in zip(sentence, first_line): # https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel
            #print(attribute, word)
            dict[attribute]=word # creating a new entry
        tuple = (sentence[0],dict)
        lines.append(tuple)
    #print(*lines , sep = " \n ")
    #print("lenght of list" , len(lines))

    category_value = [value[0] for value in lines] # prints the first value of the tuple in the list
    total_number_categories = (len(category_value)-1) # since play tennis is in the list
    first_value = category_value[1]
    global second_value
    first_counter = 0
    second_counter = 0
    for value in category_value[1:]:
        if(first_value != value):
            second_value = value
            second_counter += 1
            print("-", value)
        else:
            print(value)
            first_counter += 1
    #print(second_value, " : ", second_counter, " and " , first_value, ":" , first_counter)
    entropy_value = entropy((second_counter/total_number_categories), (first_counter/total_number_categories))
    print("entropy value" , entropy_value)
    #print(str(category_value))

#def atributes_gain():
#    for i in range len(lines):






def entropy(Yes, No):
        entropy = -(Yes*(math.log(Yes)/math.log(2))) - (No) * (math.log(No)/math.log(2))
        return (entropy)

#def gain(Entropy(s) - )

ReadFile("TennisDataSet.txt")
#atributes_gain()
