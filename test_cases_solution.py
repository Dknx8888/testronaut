import unittest

from solution import CircularDeque, CDLL, CDLLCD


class CircularDequeTest(unittest.TestCase):

    def test_init(self):
        deque = CircularDeque()
        self.assertEqual(deque.capacity, 4)
        self.assertEqual(deque.size, 0)
        self.assertEqual(deque.queue, [None] * 4)
        self.assertIsNone(deque.front)
        self.assertIsNone(deque.back)

        deque = CircularDeque([1, 2, 3], front=1, capacity=5)
        self.assertEqual(deque.capacity, 5)
        self.assertEqual(deque.size, 3)
        self.assertEqual(deque.queue, [None, 1, 2, 3, None])
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
        deque = CircularDeque([1])
        self.assertFalse(deque.is_empty())

    def test_front_element(self):
        deque = CircularDeque()
        self.assertIsNone(deque.front_element())
        deque = CircularDeque([1, 2, 3], front=1)
        self.assertEqual(deque.front_element(), 1)

    def test_back_element(self):
        deque = CircularDeque()
        self.assertIsNone(deque.back_element())
        deque = CircularDeque([1, 2, 3], front=1)
        self.assertEqual(deque.back_element(), 3)

    def test_enqueue(self):
        deque = CircularDeque(capacity=4)
        deque.enqueue(1)
        self.assertEqual(deque.size, 1)
        self.assertEqual(deque.front, 0)
        self.assertEqual(deque.back, 0)
        self.assertEqual(deque.queue, [1, None, None, None])

        deque.enqueue(2, front=False)
        self.assertEqual(deque.size, 2)
        self.assertEqual(deque.front, 0)
        self.assertEqual(deque.back, 1)
        self.assertEqual(deque.queue, [1, 2, None, None])

        deque.enqueue(0)
        self.assertEqual(deque.size, 3)
        self.assertEqual(deque.front, 3)
        self.assertEqual(deque.back, 1)
        self.assertEqual(deque.queue, [1, 2, None, 0])

        deque.enqueue(3, front=False)
        self.assertEqual(deque.size, 4)
        self.assertEqual(deque.capacity, 4)
        self.assertEqual(deque.front, 3)
        self.assertEqual(deque.back, 2)
        self.assertEqual(deque.queue, [1, 2, 3, 0])

        deque.enqueue(4)
        self.assertEqual(deque.size, 5)
        self.assertEqual(deque.capacity, 8)
        self.assertEqual(deque.front, 7)
        self.assertEqual(deque.back, 2)
        self.assertEqual(deque.queue, [1, 2, 3, 0, None, None, None, 4] + [None] * 3)

    def test_dequeue(self):
        deque = CircularDeque([1, 2, 3], front=1, capacity=5)
        val = deque.dequeue()
        self.assertEqual(val, 1)
        self.assertEqual(deque.size, 2)
        self.assertEqual(deque.front, 2)
        self.assertEqual(deque.back, 3)
        self.assertEqual(deque.queue, [None, 1, 2, 3, None])

        val = deque.dequeue(front=False)
        self.assertEqual(val, 3)
        self.assertEqual(deque.size, 1)
        self.assertEqual(deque.front, 2)
        self.assertEqual(deque.back, 2)
        self.assertEqual(deque.queue, [None, 1, 2, 3, None])

        val = deque.dequeue()
        self.assertEqual(val, 2)
        self.assertEqual(deque.size, 0)
        self.assertIsNone(deque.front)
        self.assertIsNone(deque.back)
        self.assertEqual(deque.queue, [None, 1, 2, 3, None])

        val = deque.dequeue()
        self.assertIsNone(val)
        self.assertEqual(deque.size, 0)

        deque = CircularDeque([1, 2, 3, 4, 5, 6, 7, 8], capacity=8)
        deque.dequeue()
        deque.dequeue()
        deque.dequeue()
        deque.dequeue()
        deque.dequeue()
        deque.dequeue()
        self.assertEqual(deque.size, 2)
        self.assertEqual(deque.capacity, 4)

    def test_grow(self):
        deque = CircularDeque([1, 2, 3, 4], capacity=4)
        deque.grow()
        self.assertEqual(deque.capacity, 8)
        self.assertEqual(deque.size, 4)
        self.assertEqual(deque.front, 0)
        self.assertEqual(deque.back, 3)
        self.assertEqual(deque.queue, [1, 2, 3, 4, None, None, None, None] + [None] * 0)

    def test_shrink(self):
        deque = CircularDeque([1, 2, 3, 4], capacity=8)
        deque.size = 2
        deque.shrink()
        self.assertEqual(deque.capacity, 4)
        self.assertEqual(deque.size, 2)
        self.assertEqual(deque.front, 0)
        self.assertEqual(deque.back, 1)
        self.assertEqual(deque.queue, [1, 2, 3, 4])

        deque = CircularDeque([1, 2, 3, 4], capacity=4)
        deque.size = 1
        deque.shrink()
        self.assertEqual(deque.capacity, 4)

        deque = CircularDeque([1, 2, 3, 4], capacity=8)
        deque.size = 2
        deque.shrink()
        self.assertEqual(deque.capacity, 4)
        self.assertEqual(deque.size, 2)
        self.assertEqual(deque.queue, [1, 2, 3, 4])
        self.assertEqual(deque.front, 0)
        self.assertEqual(deque.back, 1)


class CDLLTest(unittest.TestCase):
    def test_init(self):
        dll = CDLL()
        self.assertEqual(dll.size, 0)
        self.assertIsNone(dll.head)

    def test_len(self):
        dll = CDLL()
        self.assertEqual(len(dll), 0)
        dll.insert(1)
        self.assertEqual(len(dll), 1)

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
        self.assertEqual(dll.head.prev.val, 3)
        self.assertEqual(dll.head.prev.next.val, 2)

    def test_remove(self):
        dll = CDLL()
        dll.remove()  # Removing from empty list should do nothing
        self.assertEqual(dll.size, 0)
        self.assertIsNone(dll.head)

        dll.insert(1)
        dll.remove()
        self.assertEqual(dll.size, 0)
        self.assertIsNone(dll.head)

        dll = CDLL()
        dll.insert(1)
        dll.insert(2)
        dll.insert(3)
        dll.remove()
        self.assertEqual(dll.size, 2)
        self.assertEqual(dll.head.val, 1)
        dll.remove(front=False)
        self.assertEqual(dll.size, 1)
        self.assertEqual(dll.head.val, 1)
        dll.remove()
        self.assertEqual(dll.size, 0)
        self.assertIsNone(dll.head)


class CDLLCDTest(unittest.TestCase):
    def test_init(self):
        cdllcd = CDLLCD()
        self.assertIsInstance(cdllcd.CDLL, CDLL)

    def test_len(self):
        cdllcd = CDLLCD()
        self.assertEqual(len(cdllcd), 0)
        cdllcd.enqueue(1)
        self.assertEqual(len(cdllcd), 1)

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
        cdllcd.enqueue(2)
        self.assertEqual(cdllcd.front_element(), 2)

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
        self.assertEqual(cdllcd.front_element(), 1)
        self.assertEqual(cdllcd.back_element(), 1)
        cdllcd.enqueue(2, front=False)
        self.assertEqual(len(cdllcd), 2)
        self.assertEqual(cdllcd.front_element(), 1)
        self.assertEqual(cdllcd.back_element(), 2)
        cdllcd.enqueue(3)
        self.assertEqual(len(cdllcd), 3)
        self.assertEqual(cdllcd.front_element(), 3)
        self.assertEqual(cdllcd.back_element(), 2)

    def test_dequeue(self):
        cdllcd = CDLLCD()
        self.assertIsNone(cdllcd.dequeue())
        cdllcd.enqueue(1)
        cdllcd.enqueue(2, front=False)
        val = cdllcd.dequeue()
        self.assertEqual(val, 1)
        self.assertEqual(len(cdllcd), 1)
        self.assertEqual(cdllcd.front_element(), 2)
        self.assertEqual(cdllcd.back_element(), 2)
        val = cdllcd.dequeue(front=False)
        self.assertEqual(val, 2)
        self.assertEqual(len(cdllcd), 0)
        self.assertIsNone(cdllcd.front_element())
        self.assertIsNone(cdllcd.back_element())

    def test_complex(self):
        cdllcd = CDLLCD()
        cdllcd.enqueue(1)
        cdllcd.enqueue(2)
        cdllcd.enqueue(3, False)
        self.assertEqual(cdllcd.dequeue(), 2)
        self.assertEqual(cdllcd.dequeue(False), 3)
        self.assertEqual(cdllcd.dequeue(), 1)
        self.assertTrue(cdllcd.is_empty())
