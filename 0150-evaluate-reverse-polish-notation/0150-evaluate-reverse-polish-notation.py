class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        
        for token in tokens:
            if token not in "+-*/":
                # Token is a number, push to stack
                stack.append(int(token))
            else:
                # Token is an operator, pop two operands
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Division truncation toward zero logic
                    # Using float division then casting to int handles negative cases correctly
                    stack.append(int(float(a) / b))
        
        # The final result is the only element left in the stack
        return stack[0]        