class ReversePolishNotation:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def calculate(self, expression):
        for item in expression:
            if item in ['+', '-', '*', '/']:
                second = self.pop()
                first = self.pop()
                self.push(eval(str(first) + item + str(second)))
            else:
                self.push(item)
        return self.pop()
