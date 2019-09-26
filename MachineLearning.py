# Advay Koranne
# Machine Learning Project
# September 14 2019


# DataStructure: dictionary

# play tennis,outlook,temperature,humidity,wind ( each one of these are the keys)
# no,sunny,hot,high,weak (one day) - one entry in the linked list [0]  contains dictioaaries where the key is the atribute

# in node class store children as dictionaries the keys for these dictionaries could be the values of the atribute, the values of the map would be node that is your child
import math
from collections import Counter


training_set = []
texting_set = []

myfile = open("TennisDataSet.txt","r")
header = myfile.readline().strip().split(',')
attributes = header[1:]

data = []
def ReadFile(file):
    for line in myfile:
        sentence = line.strip().split(",")
    #    print(sentence)
        dict = {}
        for value, attribute in zip(sentence[1:], header[1:]): # https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel
            dict[attribute]=value # creating a new entry
        tuple = (sentence[0],dict)
        data.append(tuple)


def call_attibutes():
    for x in header[1:]:
        atributes_gain(data, x)
        print("---------------")

def atributes_gain(set, attibute):
    sub_set = []
    first_value = [value[1] for value in set] # list of dict from second value of tuple in list

    #print(first_value) # https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel
    for x in range(len(first_value)):
        value = (first_value[x].get(attibute))
        sub_set.append(value)

    sorted = Counter(sub_set)
    sub_list_of_attibutes = []
    for key in sorted:
        attibutes_sub_list = []
        for x in range(0,len(set)):
            if(key in set[x][1].values()):
                attibutes_sub_list.append(set[x])

        sub_list_of_attibutes.append(attibutes_sub_list)
    print(sub_set)
    entropy = (entropy_categories(set))
    print("entropy of set" , entropy)
    size_of_set = len(set)
    for x in range(len(sub_list_of_attibutes)):
        values_for_entropy = sub_list_of_attibutes[x]
        sub_entropy = (len(sub_list_of_attibutes[x])/size_of_set)*entropy_categories(values_for_entropy)
        entropy = entropy - sub_entropy
    print("entropy of" , attibute, ":", entropy)


# N.B: divide the divided cateogies of the yes and the no, by the category type
def entropy_categories(set):
    category_value = [value[0] for value in set] # prints the first value of the tuple in the list
    total_number_categories = (len(category_value)) # since play tennis is in the list
    sorted = Counter(category_value)
    len_of_list = len(sorted)

    entropyV = 0
    for key in sorted.values():
    #    print(key)
        value = key/total_number_categories
        entropy2 = (value*(math.log(value)/math.log(2)))
        entropyV = entropyV - entropy2
    return(entropyV)

ReadFile("TennisDataSet.txt")
call_attibutes()
