class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack= []
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            if val <= self.min_stack[-1] :
                self.min_stack.append(val)
            else:
                temp = self.min_stack[-1]
                self.min_stack.append(temp)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:

        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.min_stack:
            return None
        else:
            return self.min_stack[-1]

