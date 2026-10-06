class MinStack:

    def __init__(self):
        self.mainstack = []
        self.minstack = []


    def push(self, val: int) -> None:
        self.mainstack.append(val)
        self.minstack.append(min(val, self.minstack[-1] if self.minstack else val))


    def pop(self) -> None:
        self.mainstack.pop()
        self.minstack.pop()


    def top(self) -> int:
        return self.mainstack[-1]


    def getMin(self) -> int:
        return self.minstack[-1]