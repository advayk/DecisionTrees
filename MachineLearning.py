# Advay Koranne
# Machine Learning Project
# September 14 2019
#  Sources reffered to:
#  1) https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
#  2) https://stackoverflow.com/questions/1663807/how-to-iterate-through-two-lists-in-parallel
#  3) https://stackoverflow.com/questions/22412258/get-the-first-element-of-each-tuple-in-a-list-in-python
#  4) https://stackoverflow.com/questions/17506947/local-variable-referenced-before-assignment-in-python
#  5) # https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
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
    myfile = open(file, "r")
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

    for element in data:
        size = size + 1
        if(size <= (frac)*(len(data))):
            training_set.append(element)
        else:
            validation_set.append(element)
            testing_set.append(element[1])

    print("total lenght: " , len(data) , "lenght of testing set: " , len(testing_set), " ... lenght of training set: " , len(training_set))
    root = (ID3(training_set,attributes))
    # root = (ID3(data,attributes)) # this will train the tree on the entire set

    tuple_of_depth_numnodes = print_tree(root, " ", 1) # call depth with 1 because the root is included already
    print("depth: " , tuple_of_depth_numnodes[0], " number of nodes: " , tuple_of_depth_numnodes[1]+1) # because the root is not included
    count = 0
    for x in range(len(testing_set)):
        if(test(root, testing_set[x], validation_set[x]) == True): # test returns true if predicted output is correct
            count = count + 1
    accuracy = (count/len(testing_set))*100
    return (accuracy, tuple_of_depth_numnodes[0], tuple_of_depth_numnodes[1]+1) # adds one because the root node is not included
    # print("Percentage accuracy" , accuracy, "%")

def atributes_gain(set, attribute):
    sub_set_of_values = []
    dict = [value[1] for value in set] # list of dict from second value of tuple in listhttps://stackoverflow.com/questions/22412258/get-the-first-element-of-each-tuple-in-a-list-in-python
    for x in range(len(dict)):
        value = (dict[x].get(attribute)) # gets the values of the specific attribute
        sub_set_of_values.append(value)

    sorted = Counter(sub_set_of_values) # counts the value in the set of the given attribute
    list_of_sub_lists = [] # attribute values sorted according to index ( list of all sub sets)
    for label in sorted:
        attributes_sub_list = []
        for x in range(0,len(set)):
            if(label == set[x][1].get(attribute)):
                attributes_sub_list.append(set[x])
        list_of_sub_lists.append(attributes_sub_list)

    entropy = (entropy_categories(set))
    size_of_set = len(set)

    for x in range(len(list_of_sub_lists)):
        values_for_entropy = list_of_sub_lists[x]
        category_entropy = entropy_categories(values_for_entropy)
        if(category_entropy < 0.0):
            print("entropy can not be negative ", category_entropy)
        sub_entropy = (len(list_of_sub_lists[x])/size_of_set)*category_entropy
        entropy =  entropy - sub_entropy
    tuple = (entropy, attribute)
    return(tuple)

def entropy_categories(set):
    category_value = [value[0] for value in set] # list of first values of the tuple ( yes, no, yes, no etc..)
    total_number_categories = (len(category_value))
    sorted = Counter(category_value) # sort the values, key is the value [yes:5, no:3] found from: https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
    len_of_list = len(sorted) # the lenght of this tells me the number of values in tennis there are 2

    total_entropy = 0
    for key in sorted.values():
        value = key/total_number_categories
        if(value == 0):
            print("error")
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
        return((Node(category_value[0], True, None, None))) #if all the values are the same: return the category

    if(len(copy_attributes) == 0):
        sorted = Counter(category_value) # sort the values
        key_with_highest_value = max(sorted, key=sorted.get) # https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        certainty = (sorted[key_with_highest_value])/sum(sorted.values())
        return(Node(key_with_highest_value, True, None, certainty)) # returns the leaf node with the most common category

    if(same == False and len(copy_attributes) != 0): # if the list is not empty or not the same then.....
        attribute_entropy = []
        for attribute in attributes[:]:
            attribute_entropy.append(atributes_gain(set, attribute))

        best_attribute = (max(attribute_entropy))[1] # gets the max attribute_entropy
        copy_attributes.remove(best_attribute) # removes that arribute from list
        list_of_examples = [value[1] for value in set] # list of dict from second value of tuple in list
        sub_set_of_values = []

        for x in range(len(list_of_examples)):
            values_of_best_attribute = (list_of_examples[x].get(best_attribute)) # dict is the list of dicationaries
            sub_set_of_values.append(values_of_best_attribute)

        sorted_value_of_attributes = Counter(sub_set_of_values) # counts the value in the set of the given attribute (puts in order)
        recursiveID3_set = []

        return_Node = Node(best_attribute, False, None, None)
        for value_of_attribute in sorted_value_of_attributes: # For each value v of that attribute
            examples_of_value = []

            for x in range(len(list_of_examples)):
                if((list_of_examples[x][best_attribute]) == value_of_attribute): #the examples that have value v and all the remaining attribute
                        examples_of_value.append(set[x])
            certainty_list = []
            if(len(examples_of_value) == 0): # not possible becasue you are creating the list of attibutes based on the examples so examples_of_Value is never 0
                for x in len(set):
                    certainty_list = set.append((set[0]))
                    values_of_examples = max(Counter(certainty_list))
                    certainty = max(Counter(certainty_list).values()/sum(certainty_list))
                    child =   Node(values_of_examples, True, None, certainty)
                    return_Node.add(value_of_attribute,child )
            else:
                child = ID3(examples_of_value, copy_attributes)
                return_Node.add_child(value_of_attribute, child)
        return(return_Node)

num_indent_per_node = [1]

def print_tree(root_node, indent, depth):
    global num_nodes

    print(indent,root_node.label) # prints the root
    children = root_node.children # gets the children of the root
    depth = depth + 1
    for child_label in children:
        num_nodes = num_nodes + 1
        print(indent + "  ", child_label) # prints the value
        num_indent_per_node.append(depth)
        print_tree(children[child_label], indent + "     ", depth)
    return (max(num_indent_per_node), num_nodes)

def test(root_node, example, validation_example):
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
            if(value.label == validation_example[0]):
                return True
            else:
                return False
        else:
            return test(value, example, validation_example)

    else:
        return False

class Node:
    def __init__(self,label,leaf,children, certainty):
        self.label = label
        self.leaf = leaf
        self.children = {} # Key is a child
        self. certainty = certainty

    def add_child(self, key, value):
        self.children[key] = value

average_percentage_correct = 0
average_depth = 0
avereage_nodes = 0
for x in range(1,11):
    print(x)
    num_nodes = 0
    tuple = ReadFile("TitanicDataSet.txt" , (0.5)) # percentage of training set
    average_percentage_correct = average_percentage_correct + tuple[0]
    average_depth = average_depth + tuple[1]
    avereage_nodes = avereage_nodes + tuple[2]

print("---------Average for 10 trials------------")
print("Average percentage: " , (average_percentage_correct/10))
print( "Average depth: " , (average_depth/10))
print("Average number of nodes: " , (avereage_nodes/10))
