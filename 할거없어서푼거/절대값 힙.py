import sys

N = int(sys.stdin.readline())
user_inputs = [int(sys.stdin.readline()) for _ in range(N)]

class AbsHeap():
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._heapify_up()

    def pop(self):
        if not self.heap:
            raise IndexError("Heap is Empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down()
        return max_item
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def _get_parent_index(self, i):
        return (i - 1) // 2

    def _get_left_child_index(self, i):
        return 2 * i + 1

    def _get_right_child_index(self, i):
        return 2 * i + 2

    def _has_parent(self, i):
        return self._get_parent_index(i) >= 0

    def _has_left_child(self, i):
        return self._get_left_child_index(i) < len(self.heap)

    def _has_right_child(self, i):
        return self._get_right_child_index(i) < len(self.heap)

    def _get_parent(self, i):
        return self.heap[self._get_parent_index(i)]

    def _get_left_child(self, i):
        return self.heap[self._get_left_child_index(i)]

    def _get_right_child(self, i):
        return self.heap[self._get_right_child_index(i)]
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _heapify_up(self):
        current_index = len(self.heap) - 1

        while self._has_parent(current_index):
            parent_index = self._get_parent_index(current_index)
            if abs(self._get_parent(current_index)) > abs(self.heap[current_index]):
                self._swap(current_index, parent_index)
                current_index = parent_index
            # 절대값이 같으면 작은 원소를 위로
            elif abs(self._get_parent(current_index)) == abs(self.heap[current_index]):
                if self._get_parent(current_index) > self.heap[current_index]:
                    self._swap(current_index, parent_index)
                    current_index = parent_index
                else:
                    break
            else:
                break

    def _heapify_down(self):
        current_index = 0

        while self._has_left_child(current_index):
            smaller_child_index = self._get_left_child_index(current_index)
            if self._has_right_child(current_index):
                if abs(self._get_right_child(current_index)) < abs(self._get_left_child(current_index)):
                    smaller_child_index = self._get_right_child_index(current_index)
                # 절대값이 같으면 작은 원소를 위로
                elif abs(self._get_right_child(current_index)) == abs(self._get_left_child(current_index)):
                    if self._get_right_child(current_index) < self._get_left_child(current_index):
                        smaller_child_index = self._get_right_child_index(current_index)

            if abs(self.heap[current_index]) < abs(self.heap[smaller_child_index]):
                break
            else:
                if abs(self.heap[current_index]) == abs(self.heap[smaller_child_index]):
                    if self.heap[current_index] > self.heap[smaller_child_index]:
                        self._swap(current_index, smaller_child_index)
                        current_index = smaller_child_index
                    else:
                        break
                else:
                    self._swap(current_index, smaller_child_index)
                    current_index = smaller_child_index

absHeap = AbsHeap()
for user_input in user_inputs:
    if user_input == 0:
        if absHeap.is_empty():
            print(0)
        else:
            print(absHeap.pop())
    else:
        absHeap.push(user_input)