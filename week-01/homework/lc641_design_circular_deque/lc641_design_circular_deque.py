class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = k
        self.deque = []


    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        # 队列已满
        if len(self.deque) == self.capacity:
            return False
        self.deque.insert(0, value)
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        # 队列已满
        if len(self.deque) == self.capacity:
            return False
        self.deque.append(value)
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        # 队列已空
        if len(self.deque) == 0:
            return False
        self.deque.pop(0)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        # 队列已空
        if len(self.deque) == 0:
            return False
        self.deque.pop()
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        # 队列已空
        if len(self.deque) == 0:
            return -1
        return self.deque[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        # 队列已空
        if len(self.deque) == 0:
            return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return not len(self.deque)

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.deque) == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()