class LRUCache(_capacity: Int) {

    class DLinkedNode(k:Int, v:Int) {
        var key:Int = k
        var value:Int = v
        var next:DLinkedNode = null
        var prev:DLinkedNode = null

    }

    // protected head and tail
    private var head:DLinkedNode = new DLinkedNode(0,0)
    private var tail:DLinkedNode = new DLinkedNode(0,0)
    head.next = tail
    tail.prev = head
    // map key to node
    private var cache:Map[Int,DLinkedNode] = Map()


    def get(key: Int): Int = {
        val node = cache.getOrElse(key,null)
        if (node != null) {
            moveToHead(node)
            node.value
        } else {
            -1
        }
    }

    def put(key: Int, value: Int) {
        var node = cache.getOrElse(key, null)
        if (node == null) {
            node = new DLinkedNode(key, value)
            cache += ((key,node))
            addToHead(node)
            if (cache.size > _capacity) {
                // remove the last-but-one node
                val removed = removeTail()
                cache = cache.-(removed.key)
            }
        } else {
            node.value = value
            moveToHead(node)
        }
    }

    def addToHead(node: DLinkedNode) {
        node.prev = head
        node.next = head.next

        head.next.prev = node
        head.next = node
    }

    def removeNode(node: DLinkedNode) {
        node.prev.next = node.next
        node.next.prev = node.prev
    }

    def moveToHead(node: DLinkedNode) {
        removeNode(node)
        addToHead(node)
    }

    def removeTail(): DLinkedNode = {
        val node = tail.prev
        removeNode(node)
        node
    }

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */