# Advay Koranne
# Machine Learning Project
# September 14 2019

from collections import Counter
import math
import random
from fractions import Fraction #https://docs.python.org/3.5/library/fractions.html

def ReadFile(file, percentage):
    data = [] # contains all the elements
    training_set = []
    testing_set = []
    validation_set = [] # it contains the same elements as the testing set except contains the category value

    frac = Fraction(percentage)
    myfile = open(file,"r")
    header = myfile.readline().strip().split(',')
    attributes = header[1:]

    for line in myfile:
        sentence = line.strip().split(",")
        dict = {}
        for value, attribute in zip(sentence[1:], header[1:]): # https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel
            dict[attribute] = value
        tuple = (sentence[0],dict)
        data.append(tuple)

    random.shuffle(data)


    size = 0

    # note this function below is for testing wether "cheating" by giving a trained set gets 100%
    # for element in data:
    #     training_set.append(element)
    #     validation_set.append(element)
    #     testing_set.append(element[1])

    for element in data:
        size = size + 1
        if(size <= (frac)*(len(data))):
            training_set.append(element)
        else:
            validation_set.append(element)
            testing_set.append(element[1])
    #print(len(data))

    #print("lenght of testing set: " , len(testing_set), " ... lenght of training set: " , len(training_set))
    root = (ID3(training_set,attributes))
    #root = (ID3(data,attributes))
    #print_tree(root, " ")
    count = 0
    for x in range(len(testing_set)):
        if(test(root, testing_set[x], validation_set[x]) == True): # test returns true if predicted output is correct
            count = count + 1
    print("Percentage accuracy: " , (count/len(testing_set))*100)

def atributes_gain(set, attribute):
    #print("Calculating gain of ", attribute)
    sub_set_of_values = []
    dict = [value[1] for value in set] # list of dict from second value of tuple in list
    for x in range(len(dict)):
        value = (dict[x].get(attribute)) # gets the values of the specific attribute
        sub_set_of_values.append(value)

    sorted = Counter(sub_set_of_values) # counts the value in the set of the given attribute
    #print(sorted)
    list_of_sub_lists = [] # attribute values sorted according to index ( list of all sub sets)
    for label in sorted:
        attributes_sub_list = []
        for x in range(0,len(set)):
            if(label == set[x][1].get(attribute)):
                attributes_sub_list.append(set[x])
        list_of_sub_lists.append(attributes_sub_list)


    #print("Len Sublist =", len(list_of_sub_lists))
    entropy = (entropy_categories(set))
    #print("Total Entropy ", entropy)
    size_of_set = len(set)

    for x in range(len(list_of_sub_lists)):
        values_for_entropy = list_of_sub_lists[x]
        category_entropy = entropy_categories(values_for_entropy)
        if(category_entropy < 0.0):
            print("ERROR: Entropy of a set cannot be negative, ", category_entropy)
        #print("Category_Entropy = ", category_entropy)
        #print("Len of sub list ", len(list_of_sub_lists[x]), " |S| = ", size_of_set)
        sub_entropy = (len(list_of_sub_lists[x])/size_of_set)*category_entropy
        #print("Sub entropy = ", sub_entropy)
        entropy =  entropy - sub_entropy

    tuple = (entropy, attribute)
    return(tuple)

def entropy_categories(set):
    #print("-------------------------------")
    category_value = [value[0] for value in set] # list of first values of the tuple ( yes, no, yes, no etc..)
    total_number_categories = (len(category_value))
    sorted = Counter(category_value) # sort the values, key is the value [yes:5, no:3]
    #print(sorted)
    len_of_list = len(sorted) # the lenght of this tells me the number of values in tennis there are 2
    #print("LEN of category_value =", len(sorted))

    total_entropy = 0
    for key in sorted.values():
        value = key/total_number_categories
        if(value == 0.0):
            print("ERROR LOG 0")
        entropy_of_category = (value*(math.log(value)/math.log(2)))
        total_entropy = total_entropy - entropy_of_category
    return(total_entropy)

def ID3(set, attributes):
    copy_attributes = attributes[:]
    category_value = [value[0] for value in set] # puts the catgeory in value in a list Yes, or No
    same = True # checks to see if its same
    for x in range(0,len(category_value)-1): # from 0 - 12
        if(category_value[x] != category_value[x+1]): #
            same = False

    # Checks to see if they all belong to the same category
    if(same == True):
        return((Node(category_value[0], True, None))) #if all the values are the same: return the category

    if(len(copy_attributes) == 0):
        sorted = Counter(category_value) # sort the values
        key_with_highest_value = max(sorted, key=sorted.get)
        #print("Counter =", sorted, " Max = ", key_with_highest_value)
        return(Node(key_with_highest_value, True, None)) # returns the leaf node with the most common category

    if(same == False and len(copy_attributes) != 0): # if the list is not empty or not the same then.....
        attribute_entropy = []
        for attribute in attributes[:]:
            #print("------------START OF NEW ATTRIBUTE FROM TOP ------------")
            attribute_entropy.append(atributes_gain(set, attribute))

        best_attribute = (max(attribute_entropy))[1] # gets the max attribute_entropy
        #print("Attribute Entropy =", attribute_entropy, "Best = ", best_attribute)

        copy_attributes.remove(best_attribute) # removes that arribute from list

        list_of_examples = [value[1] for value in set] # list of dict from second value of tuple in list

        sub_set_of_values = []

        for x in range(len(list_of_examples)):
            values_of_best_attribute = (list_of_examples[x].get(best_attribute)) # dict is the list of dicationaries
            sub_set_of_values.append(values_of_best_attribute)


        sorted_value_of_attributes = Counter(sub_set_of_values) # counts the value in the set of the given attribute (puts in order)

        recursiveID3_set = []

        return_Node = Node(best_attribute, False, None)
        for value_of_attribute in sorted_value_of_attributes: # For each value v of that attribute
            examples_of_value = []
            for x in range(len(list_of_examples)):
                if((list_of_examples[x][best_attribute]) == value_of_attribute): #the examples that have value v and all the remaining attribute
                        examples_of_value.append(set[x])
            if(len(examples_of_value) == 0):
                print("**********no more values**************")
            else:
                child = ID3(examples_of_value, copy_attributes)
                return_Node.add_child(value_of_attribute, child)
        return(return_Node)

def print_tree(root_node, indent):
    print(indent,root_node.label) # prints the root
    children = root_node.children # gets the children of the root
    for child_label in children:
        print(indent + "  ", child_label) # prints the value
        print_tree(children[child_label], indent + "     ")

def test(root_node, example, validation_example):
    # print("testing" , example)
    # print("Validation: " , validation_example)
    # print("-----------------------------")
    if(root_node.leaf == True):
        if (root_node.label == validation_example[0]):
            return True
        else:
            return False

    value_of_example = example[root_node.label] # gets the value of the root_attribute
    children = root_node.children
    if(value_of_example in children):
        value = children[value_of_example]
        if(value.leaf == True):
            #print("VLEX =", validation_example)
            if(value.label == validation_example[0]):
                #print("VLYES ", value.label)
                return True
            else:
                #print("VLNO ", value.label)
                return False
        else:
            return test(value, example, validation_example)

    else:
        #print("Error: Insufficient training, missing values. ", value_of_example)
        return False

class Node:
    def __init__(self,label,leaf,children):
        self.label = label
        self.leaf = leaf
        self.children = {} # Key is a child

    def add_child(self, key, value):
        self.children[key] = value


#ReadFile("nursery.data" , (0.35)) # percentage of training set
#ReadFile("TitanicDataSet.txt" , (0.35)) # percentage of training set
#ReadFile("TennisDataSet.txt" , (0.9999)) # percentage of training set
for x in range(1,100):
    #print(x)
    ReadFile("PrimaryTumorDataSet.txt" , (0.5)) # percentage of training set
