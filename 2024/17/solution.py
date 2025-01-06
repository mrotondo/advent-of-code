import re

input_file = open("input.txt")
registers = {}
registers[4] = int(re.search(r'\d+', input_file.readline()).group(0))
registers[5] = int(re.search(r'\d+', input_file.readline()).group(0))
registers[6] = int(re.search(r'\d+', input_file.readline()).group(0))
_ = input_file.readline()
program = list(map(int, re.search(r'(\d,?)+', input_file.readline()).group(0).split(",")))

def combo_operand_value(combo_operand, registers):
  match combo_operand:
    case x if 0 <= x <= 3:
      return combo_operand
    case x if 4 <= x <= 6:
      return registers[x]
    case _:
      raise ValueError

# 1: write A % 8 to B (A:41644071 => B:7)
# 2: write B ^ 2 to B (B:7 => B:5)
# 3: write int(A / 2^B) to C (A:41644071, B:5 => C:1301377)
# 4: write B ^ 7 to B (B:5 => B:2)
# 5: write B ^ C to B (B:2, C: 1301377 => B:1301379)
# 6: write int(A / 8) to A (A:41644071 => A:5205508)
# 7: output B % 8 (B:1301379 => "3")

output = ""
instruction_pointer = 0
while instruction_pointer < len(program):
  print(instruction_pointer)
  opcode = program[instruction_pointer]
  operand = program[instruction_pointer + 1]
  match opcode:
    case 0:
      numerator = registers[4]
      denominator = 2**combo_operand_value(operand, registers)
      registers[4] = int(numerator/denominator)
    case 1:
      registers[5] = registers[5] ^ operand
    case 2:
      registers[5] = combo_operand_value(operand, registers) % 8
    case 3:
      if registers[4] != 0:
        instruction_pointer = operand
        continue
    case 4:
      registers[5] = registers[5] ^ registers[6]
    case 5:
      value = combo_operand_value(operand, registers) % 8
      if len(output) > 0:
        output += ","
      output += "{}".format(value)
    case 6:
      numerator = registers[4]
      denominator = 2**combo_operand_value(operand, registers)
      registers[5] = int(numerator/denominator)
    case 7:
      numerator = registers[4]
      denominator = 2**combo_operand_value(operand, registers)
      registers[6] = int(numerator/denominator)
  instruction_pointer += 2

print(output)