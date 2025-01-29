class EvalExpression:
    @staticmethod
    def doMath(op, num1, num2):
        """
        Perform mathematical operations based on the operator.
        Args:
            op (str): The operator ('+', '-', '*', '/')
            num1 (int/float): The first operand
            num2 (int/float): The second operand
        Returns:
            The result of the operation
        """
        if op == "*":
            return num1 * num2
        elif op == "/":
            return num1 / num2
        elif op == "+":
            return num1 + num2
        else:
            return num1 - num2

    def evaluate(self, x: str):
        """
        Evaluates a given infix expression (string).
        Args:
            x (str): The expression to evaluate (only supports numbers and basic operators)
        Returns:
            The evaluated result as an integer/float.
        """
        # Operator precedence
        prec = {
            "*": 3,
            "/": 3,
            "+": 2,
            "-": 2,
            "(": 1
        }

        opList = []  # Stack for operators
        postfixList = []  # Output list
        tokenList = ""  # Temporary storage for numbers

        # Iterate through the given string
        for token in x:
            if token in "0123456789":  # If token is a number
                tokenList += token
            elif token in "+-*/()":  # If token is an operator or parenthesis
                if tokenList:
                    postfixList.append(tokenList)
                    tokenList = ""

                if token == '(':
                    opList.append(token)
                elif token == ')':
                    topToken = opList.pop()
                    while topToken != '(':
                        postfixList.append(topToken)
                        topToken = opList.pop()
                else:
                    while (len(opList) > 0) and (prec[opList[-1]] >= prec[token]):
                        postfixList.append(opList.pop())
                    opList.append(token)

        if tokenList:  # Append any remaining number
            postfixList.append(tokenList)

        while len(opList) > 0:  # Append remaining operators
            postfixList.append(opList.pop())

        # Evaluate the postfix expression
        operandList = []
        for token in postfixList:
            if token.isdigit():  # If token is a number
                operandList.append(int(token))
            else:  # If token is an operator
                op2 = operandList.pop()
                op1 = operandList.pop()
                final = EvalExpression.doMath(token, op1, op2)
                operandList.append(final)

        return operandList[0]  # Final evaluated result


P = EvalExpression() #print(P.evaluate("A * B + C * D"))
print(P.evaluate("( A + B ) * C - ( D - E ) * ( F + G )"))
print(P.evaluate("1000 - 400 / 2"))

