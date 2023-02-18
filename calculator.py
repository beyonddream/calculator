#!/usr/bin/env python3

######################################################
#  add_sub_opt := '+' | '-'
#  mul_div_opt := '*' | '/'
#  digits := [0..9]
#  
#  expr := term {add_sub_opt term}
#  term := atom {mul_div_opt atom}
#  atom := digits | '(' expr ')'
######################################################

from typing import List, Tuple

class InvalidExpression(Exception):
    pass

class InvalidDivisor(ArithmeticError):
    pass

class InvalidSymbol(Exception):
    pass

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> int:
    if b == 0:
        raise InvalidDivisor 
    else:
        return a / b

# ordered set of symbols from most binding to least
VALID_OPERATORS = ['/', '*', '-', '+']

# valid digits of operands
VALID_OPERAND_DIGITS  = tuple(i for i in range(0, 10))

# ignorable characters
IGNORE_CHAR = [' ', '\t']

# open parenthesis signal entering a sub-expression
OPEN_CONTEXT = '('

# close parenthesis signal leaving a sub-expression
CLOSE_CONTEXT = ')'

def evaluate(c: chr, operand_stack: List[int], operator_stack: List[int]):
    try:
        if c == '+':
            operand_stack.append(
                add(operand_stack.pop(),
                    operand_stack.pop()))
        elif c == '-':
            right = operand_stack.pop()
            operand_stack.append(
                subtract(operand_stack.pop(),
                        right))
        elif c == '*':
            operand_stack.append(
                multiply(operand_stack.pop(),
                    operand_stack.pop()))
        elif c == '/':
            right = operand_stack.pop()
            operand_stack.append(
                divide(operand_stack.pop(),
                        right))
        else:
            raise InvalidSymbol
    except Exception:
        raise InvalidExpression(f'Error occured while evaluating operator {c}')

def parse(expr: str) -> Tuple[int, int]:
    """ Main parser to evaluate simple arithmetic expressions."""
    
    def parse_inner(expr: str, start: int, end: int) -> Tuple[int, int]:
        current_index = start
        n = end
        
        # stack to store the operator's
        operator_stack = []
        # stack to store the operand and result of expression evaluation
        operand_stack = []

        while current_index < n:
            c = expr[current_index]
            if c in IGNORE_CHAR:
                current_index += 1
            elif (c not in VALID_OPERATORS) and \
                c != OPEN_CONTEXT and c != CLOSE_CONTEXT and \
                    (int(c) not in VALID_OPERAND_DIGITS):
                raise InvalidExpression(f'Invalid character {c} found at index {current_index}')
            else:
                if c == OPEN_CONTEXT:
                    sum, next_index = parse_inner(expr, current_index + 1, n)
                    operand_stack.append(sum)
                    current_index = next_index + 1
                elif c == CLOSE_CONTEXT:
                    break
                else:
                    if c in VALID_OPERATORS:
                        if len(operator_stack) == 0:
                            operator_stack.append(c)
                        else:
                            op = operator_stack[-1]
                            if VALID_OPERATORS.index(c) < \
                                VALID_OPERATORS.index(op):
                                operator_stack.append(c)
                            else:
                                while operator_stack and \
                                    VALID_OPERATORS.index(operator_stack[-1]) <= \
                                        VALID_OPERATORS.index(c):
                                    evaluate(operator_stack.pop(),
                                        operand_stack, operator_stack)
                                operator_stack.append(c)
                    else:
                        # scan until all digits are accrued.
                        s = c
                        next_index = current_index + 1
                        while next_index < n:
                            try:
                                if int(expr[next_index]) in VALID_OPERAND_DIGITS:
                                    s += expr[next_index]
                                    next_index += 1
                            except ValueError:
                                break
                        current_index = next_index - 1
                        operand_stack.append(int(s))

                    current_index += 1

        while operator_stack:
            op = operator_stack.pop()
            evaluate(op, operand_stack, operator_stack)
            
        if len(operand_stack) != 1:
            raise InvalidExpression(f'Incorrect number of operands passed.')
        
        return operand_stack.pop(), current_index

    try:
        sum, _ = parse_inner(expr, 0, len(expr))
        return sum
    except Exception as e:
        print(f'Error evaluating expression {expr}: {e}')    


if __name__ == '__main__':
    expression = input()
    sum = parse(expression)
    print(f'Evaluation of expression: {expression} is {sum}')