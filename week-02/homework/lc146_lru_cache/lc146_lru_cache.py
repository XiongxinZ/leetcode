class DLinkedList:
    def __init__(self, key=0, value=0) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# 用双向链表保头去尾
class LRUCache:

    def __init__(self, capacity: int):
        # 双链的头尾保护节点
        self.head = DLinkedList()
        self.tail = DLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head
        # 存储的临界值
        self.capacity = capacity
        self.size = 0
        # 为了实现O(1)，用哈希表存储每个key所映射的节点
        self.cache = dict()


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果对应的key存在，通过哈希表定位节点，把它移到头部根据LRU原则
        node = self.cache[key]
        self.moveToHead(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 创建一个新的节点
            node = DLinkedList(key, value)
            # 在哈希表做映射关系
            self.cache[key] = node
            # 根据LRU原则，直接添加到头部
            self.addToHead(node)
            self.size += 1
            # 判断是否超过临界容量
            if self.size > self.capacity:
                # 若超出，去尾
                to_removed = self.removeTail()
                # 删除哈希表对应关系
                self.cache.pop(to_removed.key)
                self.size -= 1
        else:
            # 如果对应的key存在，通过哈希表定位节点，修改它的值，把它移到头部根据LRU原则
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        # 先更新新人节点插队前后的节点
        node.prev = self.head
        node.next = self.head.next
        # 然后再更新老人节点的人际关系
        # 顺序很重要，否则节点的引用不对
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        # 节点删除，前后等价
        node.next.prev = node.prev
        node.prev.next = node.next

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        # 删除尾巴保护节点的前一个节点
        node = self.tail.prev
        self.removeNode(node)
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)