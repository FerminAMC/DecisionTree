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
            for i in range(len(data_table)):
                for j in range(len(data_table[i])):
                    if(self.position == j):
                        self.values[data_table[i][j]][data_table[i][table_width]] += 1
        else: # We are working with the answer node
            for i in self.values:
                self.values[i] = 0
            for i in range(len(data_table)):
                self.values[data_table[i][table_width]] += 1


    def calc_entropy(self):
        if(self.answer == True):
            entropy = 0
            total = 0
            for i in self.values:
                total += self.values[i]
            for i in self.values:
                entropy -= (self.values[i]/total) * math.log((self.values[i]/total), 2)
            return(entropy)
        else:
            total_entropy = 0
            total = 0
            for i in self.values:
                for j in self.values[i]:
                    total += self.values[i][j]
            for i in self.values:
                i_total = 0
                probability = 0
                entropy = 0
                for j in self.values[i]:
                    i_total += self.values[i][j]
                for j in self.values[i]:
                    probability = self.values[i][j]/i_total
                    if(probability > 0):
                        entropy -= probability * math.log(probability, 2)
                total_entropy += (i_total/total)*entropy
            return(total_entropy)

    def select_best(self, nodes):
        best = None
        info_gained = 0
        answer_entropy = 0
        for node in nodes:
            if(node.answer == True):
                answer_entropy = node.calc_entropy()
        for node in nodes:
            if(info_gained < answer_entropy - node.calc_entropy()):
                info_gained = answer_entropy - node.calc_entropy()
                best = node
        return best

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
    Node().select_best(nodes)
