class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for i in tokens:
            if i == '+':
                stack.append(stack.pop()+stack.pop())
            elif i == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif i == '/':
                c, d = stack.pop(), stack.pop()
                stack.append(int(d/c))
            elif i == '*':
                stack.append(stack.pop()*stack.pop())
            else:
                 stack.append(int(i))
        return stack[0]