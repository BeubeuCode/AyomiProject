class ReversePolishNotation:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def calculate(self, expression):
        # operator list with lambda functions
        operators = {'+': lambda x, y: x + y,
                     '-': lambda x, y: x - y,
                     '*': lambda x, y: x * y,
                     '/': lambda x, y: x / y}
        for token in expression.split():
            if token.isdigit():
                self.stack.append(float(token))
            elif token in operators:
                if len(self.stack) < 2:
                    raise ValueError("Invalid expression: Not enough operands for operator")
                else:
                    operand2 = self.stack.pop()
                    operand1 = self.stack.pop()
                    result = operators[token](operand1, operand2)
                    self.stack.append(result)
            else:
                raise ValueError("Invalid expression: Unknown operator")


        if len(self.stack) != 1:
            raise ValueError("Invalid expression: Too many operands")

        return self.stack[0]