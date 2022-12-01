import re

def evaluate_expression1(expression_line, lhs = 0, operator = '', num_chars_evaluated=0):
  if len(expression_line) == 0:
    return (lhs, num_chars_evaluated)
  char = expression_line[0]
  if re.search(r'\d', char):
    x = int(char)
    if operator == '+':
      return evaluate_expression1(expression_line[1:], lhs=lhs + x, num_chars_evaluated=num_chars_evaluated+1)
    elif operator == '*':
      return evaluate_expression1(expression_line[1:], lhs=lhs * x, num_chars_evaluated=num_chars_evaluated+1)
    else:
      return evaluate_expression1(expression_line[1:], lhs=x, num_chars_evaluated=num_chars_evaluated+1)
  elif char == '(':
    (x, num_subexpr_chars) = evaluate_expression1(expression_line[1:], num_chars_evaluated=1)
    if operator == '+':
      return evaluate_expression1(expression_line[num_subexpr_chars:], lhs=lhs + x, num_chars_evaluated=num_chars_evaluated+num_subexpr_chars)
    elif operator == '*':
      return evaluate_expression1(expression_line[num_subexpr_chars:], lhs=lhs * x, num_chars_evaluated=num_chars_evaluated+num_subexpr_chars)
    else:
      return evaluate_expression1(expression_line[num_subexpr_chars:], lhs=x, num_chars_evaluated=num_chars_evaluated+num_subexpr_chars)
  elif char == ')':
    return (lhs, num_chars_evaluated+1)
  elif char == '+' or char == '*':
    return evaluate_expression1(expression_line[1:], lhs=lhs, operator=char, num_chars_evaluated=num_chars_evaluated+1)
  raise ArithmeticError('bad char {0}'.format(char))

class PolishNotationExpression:
  def collapse(self):
    raise NotImplementedError()

class NumberExpression(PolishNotationExpression):
  def __init__(self, number):
    self.number = number

class ParentheticalExpression(PolishNotationExpression):
  def __init__(self, sub_expression):
    self.subexpression = subexpression

class OperatorExpression(PolishNotationExpression):

  def __init__(self, operator, left_hand_expression, right_hand_expression):
    self.operator = operator
    self.left_hand_expression = left_hand_expression
    self.right_hand_expression = right_hand_expression

  def collapse(self):
    return 


def parse_expression(expr_line):
  print(expr_line)
  if len(expr_line) == 0:
    return ()
  lhs = expr_line[0]
  if re.search(r'\d', lhs):
    if len(expr_line) == 1:
      return lhs
    op = expr_line[1]
    return (op, lhs, parse_expression(expr_line[2:]))
  elif lhs == '(':
    return

def collapse_expression(parsed_expr):
  else:
    op = parsed_expr[0]
    lhs = parsed_expr[1]
    rhs = parsed_expr[2]
    if op == '+':
      if isinstance(rhs, str):
        return int(lhs) + int(rhs)
      else:
        return collapse_expression()
      return 

f = open('input_test2.txt')
ls = [l for l in f.readlines() if len(l) > 0]
compressed_lines = map(lambda s: re.sub(r'\s', '', s), ls)
results = map(evaluate_expression1, compressed_lines)
total = sum(map(lambda result_and_length: result_and_length[0], results))

print(total)

print(parse_expression(compressed_lines[0]))

# 1 + 2 * 3 + 4 * 5 + 6
# (+ 1 (* 2 (+ 3 (* 4 (+ 5 6)))))
# (+ (* (+ (* (+ 1 2) 3) 4) 5) 6)


# 2 * 3 + (4 * 5)
# ('*', 2, ('+', 3, ('(', ('*', 4, 5,))))

# 2 3 * 4 5 * +

# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
# ('(', ('*', ('(', ('+', 2, ('*', 4, 9)), ))