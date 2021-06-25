class MyCircularDeque(_k: Int) {

    /** Initialize your data structure here. Set the size of the deque to be k. */
    val cap = _k
    var deque = List.empty[Int]

    /** Adds an item at the front of Deque. Return true if the operation is successful. */
    def insertFront(value: Int): Boolean = {
        if (deque.length == cap) false else {
            deque = value :: deque
            true
        }
    }

    /** Adds an item at the rear of Deque. Return true if the operation is successful. */
    def insertLast(value: Int): Boolean = {
        if (deque.length == cap) false else {
            deque = deque :+ value
            true
        }
    }

    /** Deletes an item from the front of Deque. Return true if the operation is successful. */
    def deleteFront(): Boolean = {
        deque match {
            case Nil => false
            case h::t => deque = t; true
        }
    }

    /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
    def deleteLast(): Boolean = {
        deque match {
            case Nil => false
            case _ => deque = deque.dropRight(1); true
        }
    }

    /** Get the front item from the deque. */
    def getFront(): Int = {
        if (deque.isEmpty) -1 else deque.head
    }

    /** Get the last item from the deque. */
    def getRear(): Int = {
        if (deque.isEmpty) -1 else deque.last
    }

    /** Checks whether the circular deque is empty or not. */
    def isEmpty(): Boolean = {
        deque.isEmpty
    }

    /** Checks whether the circular deque is full or not. */
    def isFull(): Boolean = {
        deque.length == cap
    }

}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * var obj = new MyCircularDeque(k)
 * var param_1 = obj.insertFront(value)
 * var param_2 = obj.insertLast(value)
 * var param_3 = obj.deleteFront()
 * var param_4 = obj.deleteLast()
 * var param_5 = obj.getFront()
 * var param_6 = obj.getRear()
 * var param_7 = obj.isEmpty()
 * var param_8 = obj.isFull()
 */