from typing import Any

class Stack:
    def __init__(self):
        self._stack = []
    
    def push(self, item) -> None:
        self._stack.append(item)
    def pop(self) -> Any:
        if not self.is_empty():
            item = self._stack[-1]
            del self._stack[-1]
            return(item)
        # 필요시
        else:
            raise IndexError
    def peek(self) -> Any:
        if not self.is_empty():            
            return self._stack[-1]
        # 필요시
        else:
            raise IndexError
    def is_empty(self) -> bool:
        return not self._stack
    def size(self) -> int:
        return len(self._stack)
    def get_self(self) -> list:
        return self._stack
    
item = 0
stack = []
#push
stack.append(item)
#pop
stack.pop()
#peek
stack[-1]
#is_empty
not stack
#size
len(stack)

    
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.get_self())
print(my_stack.pop())
print(my_stack.get_self())
print(my_stack.peek())
print(my_stack.get_self())
