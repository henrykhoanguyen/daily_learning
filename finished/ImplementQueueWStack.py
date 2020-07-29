class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.popStack = []
        self.pushStack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.pushStack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # Move elements from push_stack to pop_stack
        self.popStack = self.pushStack[::-1]
        self.pushStack.clear()

        # Get element on top of pop_stack
        tmp = self.popStack.pop()

        # Move elements from pop_stack to push_stack
        self.pushStack = self.popStack[::-1]
        self.popStack.clear()

        return tmp

    def peek(self) -> int:
        """
        Get the front element.
        """
        # Move elements from push_stack to pop_stack
        self.popStack = self.pushStack[::-1]
        self.pushStack.clear()

        # Get element on top of pop_stack
        temp = self.popStack[-1]

        # Move elements from pop_stack to push_stack
        self.pushStack = self.popStack[::-1]
        self.popStack.clear()

        return temp

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if len(self.pushStack) <= 0 else False

queue = MyQueue()

queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.peek())
print(queue.empty())