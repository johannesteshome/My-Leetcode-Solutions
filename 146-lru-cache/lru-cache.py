class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        # self.cache = defaultdict()
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    # remove Item
    def remove(self, node):
        
        # print(node.val, 'node')
        previousNode = node.prev
        nextNode = node.next

        previousNode.next = nextNode
        nextNode.prev = previousNode
        
    # insert at the right
    def insert(self, node):
        previousNode = self.right.prev

        previousNode.next = node
        node.prev = previousNode
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        # print('get', key)

        if key in self.cache:
            # print(self.cache)
            # print('get called it', self.cache[key].val)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # print('put', key)    
        
        if key in self.cache:
            # print('put called it')
            self.remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            # print('put called it')
            delKey = self.left.next.key
            self.remove(self.left.next)
            del self.cache[delKey]
        
        newNode = Node(key, value)
        self.insert(newNode)
        self.cache[key] = newNode



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)