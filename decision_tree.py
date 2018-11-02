# A great source for understanding how to calculate the Entropy and
# Information gained
# https://www.saedsayad.com/decision_tree.htm

# Import libraries
import math
import fileinput
import re

class Node():
    def __init__(self):
        self.name = ""
        self.attributes = []
        self.position = 0

# Calculation of entropy
def calc_entropy(nodes, data_table):
    entropy = 0
    answer_node = nodes[len(nodes)-1]
    counter = {}
    for attribute in answer_node.attributes:
        counter[attribute] = 0
    for i in range(len(data_table)):
        counter[data_table[i][len(data_table[i])-1]] += 1
    for attribute in counter:
        if counter[attribute] > 0:
            entropy -= (counter[attribute] / len(data_table)) * math.log((counter[attribute] / len(data_table)), 2)
    return entropy


# Information gain for every node
def calc_info_gain(nodes, data_table, att, ent):
    ifo_gain = 0
    entropy = 0
    for node in nodes:
        for attribute in node.attributes:
            if(node.name == att):
                split = split_data(data_table, attribute, node.position)
                entropy += (len(split) / len(data_table)) * calc_entropy(nodes, split)
    info_gain = ent - entropy
    return info_gain

# Splitting data to format it for recursion
def split_data(data_table, attribute, position):
    split_data = [row for row in data_table if attribute == row[position]]
    #pp.pprint(split_data)
    return split_data

# Building the tree
def id3(nodes, data_table, entropy, depth):
    tabs = "  " * depth
    if entropy == 0:
        print(tabs + "ANSWER: "+ data_table[0][nodes[len(nodes)-1].position])
    else:
        info_gain = 0
        for node in nodes:
            if(node != nodes[len(nodes)-1]):
                aux = calc_info_gain(nodes, data_table, node.name, entropy)
                if(aux > info_gain):
                    info_gain = aux
                    best = node
        if(info_gain != 0):
            for attribute in best.attributes:
                print(tabs + best.name + ": " + attribute)
                split = split_data(data_table, attribute, best.position)
                recursive_entropy = calc_entropy(nodes, split)
                if(len(split) > 0):
                    id3(nodes, split, recursive_entropy, depth + 1)
# Parsing the node
def parse_node(string, nodes):
    # Format the attributes to add it to the dictionary of attributes
    string = string.split(' ')
    name = string[0].replace(' ','')
    node = Node()
    if not nodes:
        node.name = name
        node.position = 0
        for element in string[1:]:
            node.attributes.append(element.replace(',','').replace(' ','').replace('}','').replace('{',''))
    else:
        position = nodes[len(nodes)-1].position + 1
        node.name = name
        node.position = position
        for element in string[1:]:
            node.attributes.append(element.replace(',','').replace(' ','').replace('}','').replace('{',''))
    nodes.append(node)

if __name__ == "__main__":
    file_input = fileinput.input()
    nodes = []
    data_table = []
    for line in file_input:
        if(line[0] != '%' and line != '\n'):
            if(line[0:10] == '@attribute' or line[0:10] == '@ATTRIBUTE'):
                l = line[11:].replace('\n','').replace('\t',' ')
                parse_node(re.sub(' +',' ', l), nodes)
            elif(line[0:5] != '@data' and line[0:5] != '@DATA' and line[0:9] != '@relation' and line[0:9] != '@REALTION'):
                data_table.append(line.replace('\n','').split(','))
    entropy = calc_entropy(nodes, data_table)
    id3(nodes, data_table, entropy, 0)
