class Node:
    def __init__(self, freq, symbol, left = None, right = None):
        self.freq = freq
        self.symbol = symbol
        self.right = right
        self.left = left
        self.huff = ''
        

from collections import Counter

def printNode(node,val='',dictionary = dict()):
    newVal = val + str(node.huff)

    if node.left:
        printNode(node.left,newVal)

    if node.right:
        printNode(node.right,newVal)

    if not node.left and not node.right:
        dictionary[node.symbol] = newVal

    return dictionary


def main(arr):
    count = dict(Counter(arr))
    nodes = []
    for key,freq in count.items():
        nodes.append(Node(freq,key))
    
    while len(nodes) >  1:
        nodes = sorted(nodes,key= lambda x: x.freq)
        left = nodes[0]
        right = nodes[1]

        left.huff = 0
        right.huff = 1

        newNode = Node(left.freq+right.freq, left.symbol+right.symbol,left,right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    x = printNode(nodes[0])
    print(x)



if __name__ == '__main__':
    arr = [('a',5),('b',9),('c',12),('d',13),('e',16),('f',45)]
    string = ''
    for i in arr:
        for j in range(i[1]):
            string+=i[0]
    main(string)