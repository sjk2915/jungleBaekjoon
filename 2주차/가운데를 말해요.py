import sys
import heapq

N = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(N)]

class MidHeap():
    def __init__(self):
        self.root = None
        self.left_heap = []  # 루트보다 작은값들이 들어갈 최대힙
        self.right_heap = [] # 루트보다 큰값들이 들어갈 최소힙

    def push(self, item):
        if self.is_empty():
            self.root = item
        else:
            if item <= self.root:
                heapq.heappush(self.left_heap, -item)
            else:
                heapq.heappush(self.right_heap, item)
            self._balance_heaps()

    def pop(self):
        if self.is_empty():
            raise IndexError("Heap is Empty")
        if not self.left_heap and not self.right_heap:
            mid_item = self.root
            self.root = None
            return mid_item
        
        mid_item = self.root
        if len(self.left_heap) >= len(self.right_heap):
            self.root = -heapq.heappop(self.left_heap)
        else:
            self.root = heapq.heappop(self.right_heap)
        return mid_item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is Empty")
        else:
            return self.root
    
    def is_empty(self):
        return self.root is None
    
    def _balance_heaps(self):
        if len(self.left_heap) > len(self.right_heap):
            new_root = -heapq.heappop(self.left_heap)
            heapq.heappush(self.right_heap, self.root)
            self.root = new_root

        elif len(self.left_heap) + 1 < len(self.right_heap):
            new_root = heapq.heappop(self.right_heap)
            heapq.heappush(self.left_heap, -self.root)
            self.root = new_root

mid_heap = MidHeap()
for num in nums:
    mid_heap.push(num)
    print(mid_heap.peek())