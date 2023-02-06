class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        self.move()
        return self.outStack.pop()

    def peek(self) -> int:
        self.move()
        peek = self.outStack.pop()
        self.outStack.append(peek)
        return peek

    def empty(self) -> bool:
        return not (self.inStack or self.outStack)
        
    def move(self) -> None:
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()