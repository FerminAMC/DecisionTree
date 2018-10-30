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
values = {'sunny': {'yes':3, 'no':2}, 'overcast': {'yes':4, 'no':0}, 'rainy': {'yes':2, 'no':3}}
answer = False
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
        if(!self.answer): # Means we have a normal node
            for i in self.values:
                for j in answer_node.values:
                    self.values[i].update({j:0})

            for i in range(len(data_table)):
                for j in range(len(data_table[i])):
                    if(self.position == j)
                        self.values[data_table[i]][data_table[i][len(data_table[i])]] += 1

        else: # We are working with the answer node
            pass

    # values is just an array of numbers
    def calc_entropy(self, values):
        entropy = 0
        total = sum(values)
        for i in range(len(values)):
            entropy -= (values[i]/total) * math.log((values[i]/total), 2)
        print(entropy)



if __name__ == "__main__":
    values = [5, 5, 4]
    root = Node()
    root.calc_entropy(values)
