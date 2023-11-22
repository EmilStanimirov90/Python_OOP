class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if element.isalpha():
            self.data.append(element)

    def pop(self):
        if self.data:
            result = self.data.pop()
            return result

    def top(self):
        if self.data:
            return self.data[-1]

    def is_empty(self):
        return not any(self.data)

    def __str__(self):
        return f'[{", ".join(reversed(self.data))}]'



#test code:

stack = Stack()

print(stack.is_empty())
print(stack)
stack.push("asd")
stack.push("helloasd")
print(stack.is_empty())
print(stack)
print(stack.top())
print(stack.pop())
print(stack)
