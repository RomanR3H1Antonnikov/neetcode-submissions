class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                if i == "+":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)
                elif i == "-":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
                elif i == "*":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a * b)
                else:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a / b))
        return stack.pop()