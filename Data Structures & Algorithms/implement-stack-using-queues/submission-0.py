class MyStack:
    def __init__(self):
        self.buf=[]

    def push(self, x: int) -> None:
        self.buf.append(x)
        

    def pop(self) -> int:
        return self.buf.pop()

        

    def top(self) -> int:
        return self.buf[-1]
        

    def empty(self) -> bool:
        return len(self.buf)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()