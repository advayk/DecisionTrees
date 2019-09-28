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
            dict[attribute] = value # creating a new entry
        tuple = (sentence[0],dict)
        data.append(tuple)
    ID3(data,attributes)

def call_attibutes():
    for x in header[1:]:
        atributes_gain(data, x)
        print("----------------------------------------------")

def atributes_gain(set, attibute):
    sub_set_of_values = []
    dict = [value[1] for value in set] # list of dict from second value of tuple in list

    for x in range(len(dict)):
        value = (dict[x].get(attibute))
        sub_set_of_values.append(value)

    sorted = Counter(sub_set_of_values) # counts the value in the set of the given attribute
    sorted_values = [] # attibute values sorted according to index
    for key in sorted:
        attibutes_sub_list = []
        for x in range(0,len(set)):
            if(key in set[x][1].values()):
                attibutes_sub_list.append(set[x])

        sorted_values.append(attibutes_sub_list)
#    print("sub set" , sub_set_of_values)
    entropy = (entropy_categories(set))
#    print("entropy of set" , entropy)
    size_of_set = len(set)

    for x in range(len(sorted_values)):
        values_for_entropy = sorted_values[x]
        sub_entropy = (len(sorted_values[x])/size_of_set)*entropy_categories(values_for_entropy)
        entropy = entropy - sub_entropy

    tuple = (entropy, attibute)
    return(tuple)


def entropy_categories(set):
    category_value = [value[0] for value in set] # list of first values of the tuple ( yes, no, yes, no etc..)
    total_number_categories = (len(category_value)) # since play tennis is in the list
    sorted = Counter(category_value) # sort the values
    len_of_list = len(sorted)

    total_entropy = 0
    for key in sorted.values():
    #    print(key)
        value = key/total_number_categories
        entropy_of_category = (value*(math.log(value)/math.log(2)))
        total_entropy = total_entropy - entropy_of_category
    return(total_entropy)


def ID3(set, attributes):
    copy_attributes = attributes[:]
    category_value = [value[0] for value in set] # prints the category value
    print(len(category_value))
    same = True
    for x in range(0,len(category_value)-1): # from 0 - 12
        if(category_value[x] != category_value[x+1]): #
            same = False

    if(same == True):
        print("all values are the same")
        return(Node(category_value[0]), True) # if all the values are the same: return the category

    if(len(copy_attributes) == 0):
        print("len of list is 0 ")
        sorted = Counter(category_value) # sort the values
        #category = (max(sorted))
        return(Node(max(sorted)), True)

#    if(len(copy_attributes) == 0):


    if(same == False and len(copy_attributes) != 0 ):
        print("len of list: ",  len(copy_attributes))
        attibute_entropy = []
        for attibute in attributes[:]:
            attibute_entropy.append(atributes_gain(set, attibute))

        best_attibute = (max(attibute_entropy))[1]
        #return(Node((best_attibute), False))
        print("Attibute: " , best_attibute)
        dict = [value[1] for value in set] # list of dict from second value of tuple in list
        #print(dict)
        sub_set_of_values = []

        for x in range(len(dict)):
            value = (dict[x].get(best_attibute))
            sub_set_of_values.append(value)

        sorted = Counter(sub_set_of_values) # counts the value in the set of the given attribute
        recursiveID3_set = []
        for key in sorted:
            print("       " , key)
            for x in range(len(dict)):
                #print(dict[x])
                #print("----------------------------------")
                if((key in dict[x].values()) == True):
                    #print(set[x])
                    recursiveID3_set.append(set[x])
        copy_attributes.remove(best_attibute)
        #print(copy_attributes)
        #print(recursiveID3_set)
        print("-----------------------------")
        if(len(copy_attributes) != 0 ):
            ID3(recursiveID3_set , copy_attributes)

class Node:
    def __init__(self,label,leaf):
        self.label = label
        self.leaf = leaf

    def child(self, leaf,label, parent):
        self.parent = parent


ReadFile("TennisDataSet.txt")
#call_attibutes()
