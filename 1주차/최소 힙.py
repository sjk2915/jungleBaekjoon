import sys
import heapq

n = int(sys.stdin.readline())
user_inputs = [int(sys.stdin.readline()) for _ in range(n)]

class MinHeap():
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
        
        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down()
        return min_item
    
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
        """새로 삽입된 요소를 올바른 위치로 이동시킵니다."""
        current_index = len(self.heap) - 1 # 새로 추가된 요소의 인덱스

        # 부모가 존재하고, 현재 노드의 값이 부모 노드보다 작으면 계속 위로 스왑
        while self._has_parent(current_index) and \
              self._get_parent(current_index) > self.heap[current_index]:
            
            parent_index = self._get_parent_index(current_index)
            self._swap(current_index, parent_index)
            current_index = parent_index # 현재 인덱스를 부모 인덱스로 업데이트

    def _heapify_down(self):
        """루트(또는 변경된) 요소를 올바른 위치로 이동시킵니다."""
        current_index = 0

        # 왼쪽 자식이 있는 동안 계속 진행 (오른쪽 자식은 없을 수 있음)
        while self._has_left_child(current_index):
            smaller_child_index = self._get_left_child_index(current_index)

            # 오른쪽 자식이 있고, 오른쪽 자식이 왼쪽 자식보다 작으면
            if self._has_right_child(current_index) and \
               self._get_right_child(current_index) < self._get_left_child(current_index):
                smaller_child_index = self._get_right_child_index(current_index)

            # 현재 노드의 값이 더 작은 자식보다 작거나 같으면 멈춤 (힙 속성 만족)
            if self.heap[current_index] <= self.heap[smaller_child_index]:
                break
            else: # 아니면 스왑하고 아래로 이동
                self._swap(current_index, smaller_child_index)
                current_index = smaller_child_index # 현재 인덱스를 더 작은 자식 인덱스로 업데이트

# 라이브러리
# min_heap = []
# for user_input in user_inputs:
#     #값 추가
#     if user_input > 0:
#         heapq.heappush(min_heap, user_input)
#     #값 출력
#     else:
#         if min_heap:
#             print(heapq.heappop(min_heap))
#         else:
#             print(0)

min_heap = MinHeap()
for user_input in user_inputs:
    #값 추가
    if user_input > 0:
        min_heap.push(user_input)
    #값 출력
    else:
        if not min_heap.is_empty():
            print(min_heap.pop())
        else:
            print(0)