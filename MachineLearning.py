# Advay Koranne
# Machine Learning Project
# September 14 2019

from collections import Counter
import math

training_set = []
texting_set = []

data = []
def ReadFile(file):
    myfile = open(file,"r")
    header = myfile.readline().strip().split(',')
    attributes = header[1:]
    list_of_nodes = []
    for line in myfile:
        sentence = line.strip().split(",")
        dict = {}
        for value, attribute in zip(sentence[1:], header[1:]): # https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel
            dict[attribute] = value # creating a new entry
        tuple = (sentence[0],dict)
        data.append(tuple)

    root = (ID3(data,attributes))
    tree(root, " ")


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
    entropy = (entropy_categories(set))
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
        value = key/total_number_categories
        entropy_of_category = (value*(math.log(value)/math.log(2)))
        total_entropy = total_entropy - entropy_of_category
    return(total_entropy)


def ID3(set, attributes):

    copy_attributes = attributes[:]
    category_value = [value[0] for value in set] # puts the catgeory in value in a list
    same = True # checks to see if its same
    for x in range(0,len(category_value)-1): # from 0 - 12
        if(category_value[x] != category_value[x+1]): #
            same = False

    # Checks to see if they all belong to the same category
    if(same == True):
        #print("all values are the same")
        return((Node(category_value[0], True, None))) #if all the values are the same: return the category

    if(len(copy_attributes) == 0):
        sorted = Counter(category_value) # sort the values
        return(Node(max(sorted), True, None)) # returns the leaf node with the most common category


    if(same == False and len(copy_attributes) != 0 ): # if the list is not empty or not the same then.....
        attibute_entropy = []
        for attibute in attributes[:]:
            attibute_entropy.append(atributes_gain(set, attibute))

        best_attibute = (max(attibute_entropy))[1] # gets the max attibute_entropy
        copy_attributes.remove(best_attibute) # removes that arribute from list

        list_of_dict_of_example = [value[1] for value in set] # list of dict from second value of tuple in list

        sub_set_of_values = []

        for x in range(len(list_of_dict_of_example)):
            values_of_best_attribute = (list_of_dict_of_example[x].get(best_attibute)) # dict is the list of dicationaries
            sub_set_of_values.append(values_of_best_attribute)

        sorted_value_of_attributes = Counter(sub_set_of_values) # counts the value in the set of the given attribute (puts in order)
        recursiveID3_set = []

        return_Node = Node(best_attibute, False, None)
        for value_of_attribute in sorted_value_of_attributes: # For each value v of that attribute
            examples_of_value = []
            for x in range(len(list_of_dict_of_example)):
                if((list_of_dict_of_example[x][best_attibute]) == value_of_attribute): #the examples that have value v and all the remaining attribute
                        examples_of_value.append(set[x])
            if(len(examples_of_value) == 0):
                print("no more values")
            else:
                child = ID3(examples_of_value, copy_attributes)
                return_Node.add_child(value_of_attribute, child)
        return(return_Node)

def tree(root_node, indent):
    copy_indent = indent
    print(copy_indent,root_node.label) # prints the root
    children = root_node.children
    for x in range(len(children)):
        print(2*copy_indent, list(children.keys())[x]) # prings the value
        tree((list(children.values())[x]), 3*copy_indent)

class Node:
    def __init__(self,label,leaf,children):
        self.label = label
        self.leaf = leaf
        self.children = {} # Key is a child

    def add_child(self, key, value):
        self.children[key] = value

ReadFile("TennisDataSet.txt")
