import queue

class HuffmanNode(object):
    def __init__(self,left=None,right=None,count=0,prefix=''):
        self.left = left
        self.right = right
        self.count = count
        self.prefix = prefix
        
    def children(self):
        return((self.left, self.right))

    def __eq__(self, string):
        if self.prefix == string:
            return True
        else:
            return False

    def __ge__(self, string):
        if self.prefix >= string:
            return True
        else:
            return False

    def __lt__(self, string):
        if self.prefix < string:
            return True
        else:
            return False

    def __gt__(self, string):
        if self.prefix > string:
            return True
        else:
            return False

'''
freq = [
    (8.167, 'a'), (1.492, 'b'), (2.782, 'c'), (4.253, 'd'),
    (12.702, 'e'),(2.228, 'f'), (2.015, 'g'), (6.094, 'h'),
    (6.966, 'i'), (0.153, 'j'), (0.747, 'k'), (4.025, 'l'),
    (2.406, 'm'), (6.749, 'n'), (7.507, 'o'), (1.929, 'p'), 
    (0.095, 'q'), (5.987, 'r'), (6.327, 's'), (9.056, 't'), 
    (2.758, 'u'), (1.037, 'v'), (2.365, 'w'), (0.150, 'x'),
    (1.974, 'y'), (0.074, 'z') ]
'''

text = "abacabad"
unique_symbols = list(set(text))
freq = [(text.count(sym), sym) for sym in unique_symbols]

def encode(frequencies):
    p = queue.PriorityQueue()
    for item in frequencies:
        p.put(item)
        
    while p.qsize() > 1:
        left,right = p.get(),p.get()
        print(left,right)
        
        if isinstance(left, HuffmanNode):
            left_count = left.count
        else:
            left_count = left[0]
            
        if isinstance(right, HuffmanNode):
            right_count = right.count
        else:
            right_count = right[0]
            
        count = left_count+right_count
        node = HuffmanNode(left,right,count)
        p.put((count,node))
    return p.get()

def create_tree(frequencies):
    p = queue.PriorityQueue()
    
    for value in frequencies:
        p.put(value)
        
    while p.qsize() > 1:
        left,right = p.get(),p.get()
        
        if isinstance(left, HuffmanNode):
            left_count = left.count
        else:
            left_count = left[0]
            
        if isinstance(right, HuffmanNode):
            right_count = right.count
        else:
            right_count = right[0]
            
        count = left_count+right_count
        node = HuffmanNode(left,right,count)
        p.put((count,node))
    return p.get()

node = create_tree(freq)

# Recursively walk the tree down to the leaves,
#   assigning a code value to each symbol
def walk_tree(node, prefix="", code={}):
    if isinstance(node[1].left[1], HuffmanNode):
        walk_tree(node[1].left,prefix+"1", code)
    else:
        code[node[1].left[1]]=prefix+"1"
    if isinstance(node[1].right[1],HuffmanNode):
        walk_tree(node[1].right,prefix+"0", code)
    else:
        code[node[1].right[1]]=prefix+"0"
    return(code)
    
code = walk_tree(node)
for i in sorted(freq, reverse=True):
    print(i[1], '{:6.2f}'.format(i[0]), code[i[1]])