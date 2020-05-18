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

def encode(frequencies):
    p = queue.PriorityQueue()
    for item in frequencies:
        p.put(item)
        
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

def huffman_encode(text):
    unique_symbols = list(set(text))
    freq = [(text.count(sym), sym) for sym in unique_symbols]
    if len(unique_symbols) > 1:
        node = create_tree(freq)
        code = walk_tree(node)
    else:
        code = {unique_symbols[0]: "0"}
    result_str = "".join([code[sym] for sym in text])
    print(str(len(unique_symbols)) + " " + str(len(result_str)))
    for i in sorted(freq, reverse=True):
        print(i[1] + ": " + code[i[1]])
    print(result_str)
    
def main():
    text = input()
    huffman_encode(text)
    
if __name__ == "__main__":
    main()