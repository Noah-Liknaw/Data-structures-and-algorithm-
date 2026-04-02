class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = type("Node", (), {})()
        self.tail = type("Node", (), {})()

        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def removeNode(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        node.next = node.prev = None

    def insertNode(self, node):
        prevNode = self.tail.prev
        prevNode.next = node
        node.prev = prevNode
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.removeNode(node)      
        self.insertNode(node)      
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeNode(node)
            self.insertNode(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.head.next
                self.removeNode(lru)
                del self.cache[lru.key]

            node = type("Node", (), {})()
            node.key = key
            node.val = value
            node.prev = node.next = None

            self.cache[key] = node
            self.insertNode(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)