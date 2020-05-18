
class PriorityQueue:
    def __init__(self):
        self.queue = []
        
    def extract_max(self):
        max_ = self.queue[0]
        print(max_)
        leaf = self.queue[-1]
        self.queue[0] = leaf
        del self.queue[-1]
        if len(self.queue) > 0:
            self.siftDown(0)

    def siftDown(self, num_i):
        num = self.queue[num_i]
        children_i1 = (num_i+1)*2-1
        children_i2 = (num_i+1)*2
        if children_i2 < 0:
            children_i2 = 0
        if children_i1 < 0:
            children_i1 = 0
        
        q_len = len(self.queue)
        if (children_i1 < q_len) and (children_i2 < q_len):
            if self.queue[children_i1] > self.queue[children_i2]:
                max_children_i = children_i1
            else:
                max_children_i = children_i2
        else:
            if children_i1 < len(self.queue):
                max_children_i = children_i1
            elif children_i2 < len(self.queue):
                max_children_i = children_i2
            else:
                return
        print()
        print(num_i)
        print(num)
        print(self.queue[max_children_i])
        print()
        if num < self.queue[max_children_i]:
            self.queue[num_i] = self.queue[max_children_i]
            self.queue[max_children_i] = num
            self.siftDown(max_children_i)
        
    def insert(self, num):
        i = len(self.queue)
        parent_i = (i-1)//2
        if parent_i < 0:
            parent_i = 0
        self.queue.append(num)
        self.siftUp(num, i, parent_i)
            
    def siftUp(self, num, num_i, parent_i):
        try:
            parent = self.queue[parent_i]
        except:
            parent = None
        if parent is None:
            return
        if num > parent:
            self.queue[parent_i] = num
            self.queue[num_i] = parent
            new_parent_i = (parent_i-1)//2
            if new_parent_i < 0:
                new_parent_i = 0
            self.siftUp(num, parent_i, new_parent_i)
       

'''
    

def main():
    p_queue = PriorityQueue()
    p_queue.insert(2)
    p_queue.insert(3)
    p_queue.insert(18)
    p_queue.insert(15)
    p_queue.insert(18)
    p_queue.insert(12)
    p_queue.insert(12)
    p_queue.insert(2)
    print(p_queue.queue)
    p_queue.insert(500)
    print(p_queue.extract_max())
    print(p_queue.queue)
    print(p_queue.extract_max())
    print(p_queue.queue)
    print(p_queue.extract_max())
    p_queue.insert(255)
    print(p_queue.extract_max())
    p_queue.insert(400)
    p_queue.insert(15)
    print(p_queue.extract_max())
    print(p_queue.queue)
    

def main():
    p_queue = PriorityQueue()
    p_queue.insert(10)
    p_queue.insert(10)
    p_queue.insert(8)
    print(p_queue.queue)
    print(p_queue.extract_max())
    print(p_queue.queue)
    print(p_queue.extract_max())
    print(p_queue.queue)
'''

def main():
    actions_cnt = int(input())
    p_queue = PriorityQueue()
    for i in range(actions_cnt):
        input_ = input().split(" ")
        action_name = input_[0]
        if action_name == "ExtractMax":
            print(p_queue.extract_max())
        if action_name == "Insert":
            num = int(input_[1])
            p_queue.insert(num)

if __name__ == "__main__":
    main()
