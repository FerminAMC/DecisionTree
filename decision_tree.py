'''
Example input:
@relation weather.symbolic

@attribute outlook {sunny, overcast, rainy}
@attribute temperature {hot, mild, cool}
@attribute humidity {high, normal}
@attribute windy {TRUE, FALSE}
@attribute play {yes, no}

@data
sunny,hot,high,FALSE,no
sunny,hot,high,TRUE,no
overcast,hot,high,FALSE,yes
rainy,mild,high,FALSE,yes
rainy,cool,normal,FALSE,yes
rainy,cool,normal,TRUE,no
overcast,cool,normal,TRUE,yes
sunny,mild,high,FALSE,no
sunny,cool,normal,FALSE,yes
rainy,mild,normal,FALSE,yes
sunny,mild,normal,TRUE,yes
overcast,mild,high,TRUE,yes
overcast,hot,normal,FALSE,yes
rainy,mild,high,TRUE,no
'''

# A great source for understanding how to calculate the Entropy and
# Information gained
# https://www.saedsayad.com/decision_tree.htm
import math

'''
@attribute input must be parsed this way:
name = "outlook"
values = ['sunny': 0, 'overcast': 0, 'rainy': 0]
if(!next_line contains '@attribute') answer = True
position = number of @attribute

@data input must be parsed this way:
data_table = [
    ["sunny","hot","high","FALSE","no"],
    ["sunny","hot","high","TRUE","no"],
    ["overcast","hot","high","FALSE","yes"],
    ["rainy","mild","high","FALSE","yes"],
    ["rainy","cool","normal","FALSE","yes"],
    ["rainy","cool","normal","TRUE","no"],
    ["overcast","cool","normal","TRUE","yes"],
    ["sunny","mild","high","FALSE","no"],
    ["sunny","cool","normal","FALSE","yes"],
    ["rainy","mild","normal","FALSE","yes"],
    ["sunny","mild","normal","TRUE","yes"],
    ["overcast","mild","high","TRUE","yes"],
    ["overcast","hot","normal","FALSE","yes"],
    ["rainy","mild","high","TRUE","no"]
]
'''
# Node class definition
'''
name = "outlook"
values = {'sunny': {'yes': 3, 'no': 2}, 'overcast': {'yes': 4, 'no': 0}, 'rainy': {'yes': 2, 'no': 3}}
answer = False
position = 0

name = "play"
values = {'yes': 9, 'no': 5}
answer = True
position = 4
'''
class Node():
    def __init__(self):
        self.name = ""
        self.values = {}
        self.children = None
        self.answer = False
        self.position = 0
        def __lt__(self, other):
            return self.entropy < other.entropy

    def is_leaf(self):
        if(self.children == None):
            return True
        return False

    def set_values(self, values):
        self.values = values

    def count_values(self, data_table, answer_node):
        table_width = len(data_table[0])-1
        if(self.answer == False): # Means we have a normal node
            for i in self.values:
                for j in answer_node.values:
                    self.values[i].update({j:0})

            #print(self.values[data_table[0][0]])
            for i in range(len(data_table)):
                for j in range(len(data_table[i])):
                    if(self.position == j):
                        self.values[data_table[i][j]][data_table[i][table_width]] += 1

        else: # We are working with the answer node
            for i in self.values:
                self.values[i] = 0

            for i in range(len(data_table)):
                self.values[data_table[i][table_width]] += 1

        print(self.values)

    def calc_entropy(self, nodes):
        if(len(nodes) == 1):
            entropy = 0
            total = 0
            if(nodes[0].answer == True):
                for i in nodes[0].values:
                    total += nodes[0].values[i]
                for i in nodes[0].values:
                    entropy -= (nodes[0].values[i]/total) * math.log((nodes[0].values[i]/total), 2)
            else:
                for i in nodes[0].values:
                    for j in nodes[0].values[i]:
                        total += nodes[0].values[i][j]
                for i in nodes[0].values:
                    i_total = 0
                    for j in nodes[0].values[i]:
                        i_total += nodes[0].values[i][j]
                    entropy -= (i_total/total) * math.log((i_total/total), 2)
            return(entropy)
        else: # The first node given must be the answer node
            total_entropy = 0
            total = 0
            for i in nodes[1].values:
                for j in nodes[1].values[i]:
                    total += nodes[1].values[i][j]
            for i in nodes[1].values:
                i_total = 0
                probability = 0
                entropy = 0
                for j in nodes[1].values[i]:
                    i_total += nodes[1].values[i][j]
                for j in nodes[1].values[i]:
                    probability = nodes[1].values[i][j]/i_total
                    if(probability > 0):
                        entropy -= probability * math.log(probability, 2)
                total_entropy += (i_total/total)*entropy
            return(total_entropy)

    def calc_entropy2(self, node):
        if(node.answer == True):
            entropy = 0
            total = 0
            for i in node.values:
                total += node.values[i]
            for i in node.values:
                entropy -= (node.values[i]/total) * math.log((node.values[i]/total), 2)
            return(entropy)
        else: # The first node given must be the answer node
            total_entropy = 0
            total = 0
            for i in node.values:
                for j in node.values[i]:
                    total += node.values[i][j]
            for i in node.values:
                i_total = 0
                probability = 0
                entropy = 0
                for j in node.values[i]:
                    i_total += node.values[i][j]
                for j in node.values[i]:
                    probability = node.values[i][j]/i_total
                    if(probability > 0):
                        entropy -= probability * math.log(probability, 2)
                total_entropy += (i_total/total)*entropy
            return(total_entropy)

if __name__ == "__main__":
    values = [5,4,5]
    root = Node()
    answer = Node()
    nodes = [answer, root]
    root.name = "outlook"
    root.values = {'sunny': {}, 'overcast': {}, 'rainy': {}}
    root.answer = False
    root.position = 0
    answer.name = "play"
    answer.values = {'yes': {}, 'no': {}}
    answer.answer = True
    answer.position = 4
    data_table = [
        ["sunny","hot","high","FALSE","no"],
        ["sunny","hot","high","TRUE","no"],
        ["overcast","hot","high","FALSE","yes"],
        ["rainy","mild","high","FALSE","yes"],
        ["rainy","cool","normal","FALSE","yes"],
        ["rainy","cool","normal","TRUE","no"],
        ["overcast","cool","normal","TRUE","yes"],
        ["sunny","mild","high","FALSE","no"],
        ["sunny","cool","normal","FALSE","yes"],
        ["rainy","mild","normal","FALSE","yes"],
        ["sunny","mild","normal","TRUE","yes"],
        ["overcast","mild","high","TRUE","yes"],
        ["overcast","hot","normal","FALSE","yes"],
        ["rainy","mild","high","TRUE","no"]
    ]
    root.count_values(data_table, answer)
    answer.count_values(data_table, answer)
    print(answer.calc_entropy2(answer))
