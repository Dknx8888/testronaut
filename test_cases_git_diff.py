import unittest

class TestCircularDeque(unittest.TestCase):

    def test_init(self):
        deque = CircularDeque()
        self.assertEqual(deque.capacity, 4)
        self.assertEqual(deque.size, 0)
        self.assertEqual(deque.queue, [None] * 4)
        self.assertIsNone(deque.front)
        self.assertIsNone(deque.back)

        deque = CircularDeque([1, 2, 3])
        self.assertEqual(deque.capacity, 4)
        self.assertEqual(deque.size, 3)
        self.assertEqual(deque.queue, [1, 2, 3, None])
        self.assertEqual(deque.front, 0)
        self.assertEqual(deque.back, 2)

        deque = CircularDeque([1, 2, 3], front=1, capacity=8)
        self.assertEqual(deque.capacity, 8)
        self.assertEqual(deque.size, 3)
        self.assertEqual(deque.queue, [None, 1, 2, 3, None, None, None, None])
        self.assertEqual(deque.front, 1)
        self.assertEqual(deque.back, 3)

    def test_len(self):
        deque = CircularDeque()
        self.assertEqual(len(deque), 0)
        deque = CircularDeque([1, 2, 3])
        self.assertEqual(len(deque), 3)

    def test_is_empty(self):
        deque = CircularDeque()
        self.assertTrue(deque.is_empty())
        deque = CircularDeque([1, 2, 3])
        self.assertFalse(deque.is_empty())

    def test_front_element(self):
        deque = CircularDeque()
        self.assertIsNone(deque.front_element())
        deque = CircularDeque([1, 2, 3])
        self.assertEqual(deque.front_element(), 1)
        deque = CircularDeque([1, 2, 3], front=1, capacity=8)
        self.assertEqual(deque.front_element(), 1)

    def test_back_element(self):
        deque = CircularDeque()
        self.assertIsNone(deque.back_element())
        deque = CircularDeque([1, 2, 3])
        self.assertEqual(deque.back_element(), 3)
        deque = CircularDeque([1, 2, 3], front=1, capacity=8)
        self.assertEqual(deque.back_element(), 3)

    def test_grow(self):
        deque = CircularDeque([1, 2, 3], capacity=4)
        deque.grow()
        self.assertEqual(deque.capacity, 8)
        self.assertEqual(deque.size, 3)
        self.assertEqual(deque.queue, [1, 2, 3, None, None, None, None, None])
        self.assertEqual(deque.front, 0)
        self.assertEqual(deque.back, 2)

        deque = CircularDeque([1, 2, 3], front=1, capacity=4)
        deque.grow()
        self.assertEqual(deque.capacity, 8)
        self.assertEqual(deque.size, 3)
        self.assertEqual(deque.queue, [1, 2, 3, None, None, None, None, None])
        self.assertEqual(deque.front, 0)
        self.assertEqual(deque.back, 2)

    def test_shrink(self):
        deque = CircularDeque([1, 2, 3], capacity=8)
        deque.shrink()
        self.assertEqual(deque.capacity, 4)
        self.assertEqual(deque.size, 3)
        self.assertEqual(deque.queue, [1, 2, 3, None])
        self.assertEqual(deque.front, 0)
        self.assertEqual(deque.back, 2)

        deque = CircularDeque([1, 2, 3], front=1, capacity=8)
        deque.shrink()
        self.assertEqual(deque.capacity, 4)
        self.assertEqual(deque.size, 3)
        self.assertEqual(deque.queue, [1, 2, 3, None])
        self.assertEqual(deque.front, 0)
        self.assertEqual(deque.back, 2)

        deque = CircularDeque([1, 2, 3], front=0, capacity=4) # Do not shrink if already minimum capacity
        deque.shrink()
        self.assertEqual(deque.capacity, 4)
        self.assertEqual(deque.size, 3)
        self.assertEqual(deque.queue, [1, 2, 3, None])
        self.assertEqual(deque.front, 0)
        self.assertEqual(deque.back, 2)

    def test_enqueue(self):
        deque = CircularDeque()
        deque.enqueue(1)
        self.assertEqual(deque.size, 1)
        self.assertEqual(deque.queue, [1, None, None, None])
        self.assertEqual(deque.front, 0)
        self.assertEqual(deque.back, 0)

        deque.enqueue(2, front=False)
        self.assertEqual(deque.size, 2)
        self.assertEqual(deque.queue, [1, 2, None, None])
        self.assertEqual(deque.front, 0)
        self.assertEqual(deque.back, 1)

        deque.enqueue(3)
        self.assertEqual(deque.size, 3)
        self.assertEqual(deque.queue, [3, 2, 1, None])
        self.assertEqual(deque.front, 2)
        self.assertEqual(deque.back, 1)

        deque.enqueue(4, front=False)
        self.assertEqual(deque.size, 4)
        self.assertEqual(deque.queue, [3, 4, 1, 2])
        self.assertEqual(deque.front, 2)
        self.assertEqual(deque.back, 3)

        deque.enqueue(5)
        self.assertEqual(deque.size, 5)
        self.assertEqual(deque.capacity, 8)
        self.assertEqual(deque.queue, [1, 2, 3, 4, 5, None, None, None])
        self.assertEqual(deque.front, 4)
        self.assertEqual(deque.back, 3)

    def test_dequeue(self):
        deque = CircularDeque([1, 2, 3, 4], capacity=4)
        val = deque.dequeue()
        self.assertEqual(val, 1)
        self.assertEqual(deque.size, 3)
        self.assertEqual(deque.queue, [None, 2, 3, 4])
        self.assertEqual(deque.front, 1)
        self.assertEqual(deque.back, 3)

        val = deque.dequeue(front=False)
        self.assertEqual(val, 4)
        self.assertEqual(deque.size, 2)
        self.assertEqual(deque.queue, [None, 2, 3, None])
        self.assertEqual(deque.front, 1)
        self.assertEqual(deque.back, 2)

        val = deque.dequeue()
        self.assertEqual(val, 2)
        self.assertEqual(deque.size, 1)
        self.assertEqual(deque.queue, [None, None, 3, None])
        self.assertEqual(deque.front, 2)
        self.assertEqual(deque.back, 2)
        
        val = deque.dequeue()
        self.assertEqual(val, 3)
        self.assertEqual(deque.size, 0)
        self.assertEqual(deque.queue, [None, None, None, None])
        self.assertEqual(deque.front, 3)
        self.assertEqual(deque.back, 3)

        val = deque.dequeue()
        self.assertIsNone(val)

        deque = CircularDeque([1,2,3,4,5,6,7,8], capacity=8)
        deque.dequeue()
        deque.dequeue()
        deque.dequeue()
        deque.dequeue()
        deque.dequeue()
        deque.dequeue()
        deque.dequeue()
        deque.dequeue()
        self.assertEqual(deque.capacity, 4)
        self.assertEqual(deque.size, 0)

class TestCDLLNode(unittest.TestCase):

    def test_init(self):
        node = CDLLNode(1)
        self.assertEqual(node.val, 1)
        self.assertIsNone(node.next)
        self.assertIsNone(node.prev)

        node2 = CDLLNode(2)
        node = CDLLNode(1, next=node2, prev=node2)
        self.assertEqual(node.val, 1)
        self.assertEqual(node.next, node2)
        self.assertEqual(node.prev, node2)

    def test_eq(self):
        node1 = CDLLNode(1)
        node2 = CDLLNode(1)
        node3 = CDLLNode(2)
        self.assertTrue(node1 == node2)
        self.assertFalse(node1 == node3)

class TestCDLL(unittest.TestCase):

    def test_init(self):
        dll = CDLL()
        self.assertEqual(dll.size, 0)
        self.assertIsNone(dll.head)

    def test_len(self):
        dll = CDLL()
        self.assertEqual(len(dll), 0)
        dll.insert(1)
        self.assertEqual(len(dll), 1)
        dll.insert(2)
        self.assertEqual(len(dll), 2)

    def test_eq(self):
        dll1 = CDLL()
        dll2 = CDLL()
        self.assertTrue(dll1 == dll2)

        dll1.insert(1)
        self.assertFalse(dll1 == dll2)
        dll2.insert(1)
        self.assertTrue(dll1 == dll2)

        dll1.insert(2)
        dll2.insert(3)
        self.assertFalse(dll1 == dll2)

    def test_insert(self):
        dll = CDLL()
        dll.insert(1)
        self.assertEqual(dll.size, 1)
        self.assertEqual(dll.head.val, 1)
        self.assertEqual(dll.head.next, dll.head)
        self.assertEqual(dll.head.prev, dll.head)

        dll.insert(2)
        self.assertEqual(dll.size, 2)
        self.assertEqual(dll.head.val, 2)
        self.assertEqual(dll.head.next.val, 1)
        self.assertEqual(dll.head.prev.val, 1)

        dll.insert(3, front=False)
        self.assertEqual(dll.size, 3)
        self.assertEqual(dll.head.val, 2)
        self.assertEqual(dll.head.next.val, 1)
        self.assertEqual(dll.head.next.next.val, 3)
        self.assertEqual(dll.head.prev.val, 3)

    def test_remove(self):
        dll = CDLL()
        dll.remove() # Removing from an empty list
        self.assertEqual(dll.size, 0)
        self.assertIsNone(dll.head)

        dll.insert(1)
        dll.remove()
        self.assertEqual(dll.size, 0)
        self.assertIsNone(dll.head)

        dll.insert(1)
        dll.insert(2)
        dll.remove()
        self.assertEqual(dll.size, 1)
        self.assertEqual(dll.head.val, 1)

        dll.insert(2, front=False)
        dll.remove(front=False)
        self.assertEqual(dll.size, 1)
        self.assertEqual(dll.head.val, 1)

        dll.insert(2)
        dll.insert(3)
        dll.remove(front=False)
        self.assertEqual(dll.size, 2)
        self.assertEqual(dll.head.val, 3)
        self.assertEqual(dll.head.next.val, 1)
        self.assertEqual(dll.head.prev.val, 1)

class TestCDLLCD(unittest.TestCase):

    def test_init(self):
        cdllcd = CDLLCD()
        self.assertIsInstance(cdllcd.CDLL, CDLL)

    def test_len(self):
        cdllcd = CDLLCD()
        self.assertEqual(len(cdllcd), 0)
        cdllcd.enqueue(1)
        self.assertEqual(len(cdllcd), 1)
        cdllcd.enqueue(2)
        self.assertEqual(len(cdllcd), 2)

    def test_is_empty(self):
        cdllcd = CDLLCD()
        self.assertTrue(cdllcd.is_empty())
        cdllcd.enqueue(1)
        self.assertFalse(cdllcd.is_empty())

    def test_front_element(self):
        cdllcd = CDLLCD()
        self.assertIsNone(cdllcd.front_element())
        cdllcd.enqueue(1)
        self.assertEqual(cdllcd.front_element(), 1)
        cdllcd.enqueue(2, front=False)
        self.assertEqual(cdllcd.front_element(), 1)

    def test_back_element(self):
        cdllcd = CDLLCD()
        self.assertIsNone(cdllcd.back_element())
        cdllcd.enqueue(1)
        self.assertEqual(cdllcd.back_element(), 1)
        cdllcd.enqueue(2, front=False)
        self.assertEqual(cdllcd.back_element(), 2)

    def test_enqueue(self):
        cdllcd = CDLLCD()
        cdllcd.enqueue(1)
        self.assertEqual(len(cdllcd), 1)
        self.assertEqual(cdllcd.CDLL.head.val, 1)

        cdllcd.enqueue(2, front=False)
        self.assertEqual(len(cdllcd), 2)
        self.assertEqual(cdllcd.CDLL.head.val, 1)
        self.assertEqual(cdllcd.CDLL.head.prev.val, 2)

        cdllcd = CDLLCD()
        cdllcd.enqueue(1)
        cdllcd.enqueue(2)
        self.assertEqual(cdllcd.CDLL.head.val, 2)
        self.assertEqual(cdllcd.CDLL.head.next.val, 1)

    def test_dequeue(self):
        cdllcd = CDLLCD()
        self.assertIsNone(cdllcd.dequeue())
        self.assertTrue(cdllcd.is_empty())

        cdllcd.enqueue(1)
        val = cdllcd.dequeue()
        self.assertEqual(val, 1)
        self.assertTrue(cdllcd.is_empty())

        cdllcd.enqueue(1)
        cdllcd.enqueue(2, front=False)
        val = cdllcd.dequeue(front=False)
        self.assertEqual(val, 2)
        self.assertEqual(len(cdllcd), 1)
        self.assertEqual(cdllcd.front_element(), 1)

        cdllcd.enqueue(2)
        val = cdllcd.dequeue()
        self.assertEqual(val, 2)
        self.assertEqual(cdllcd.front_element(), 1)
        
        cdllcd.dequeue()
        self.assertTrue(cdllcd.is_empty())

if __name__ == '__main__':
    unittest.main()
