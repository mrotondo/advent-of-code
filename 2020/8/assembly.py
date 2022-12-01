def parse_line(l):
    return (l[:3], int(l[4:-1]))

def execute_line(instruction, operand, program_counter, acc):
    if (instruction == "acc"):
        return (program_counter + 1, acc + operand)
    elif (instruction == "jmp"):
        return (program_counter + operand, acc)
    elif (instruction == "nop"):
        return (program_counter + 1, acc)

def run_program(program):
    acc = 0
    executed_lines = set()
    program_counter = 0
    while(program_counter not in executed_lines):
        if program_counter == len(program):
            return (True, acc)
        elif program_counter > len(program):
            return (False, acc)
        (instruction, operand) = program[program_counter]
        executed_lines.add(program_counter)
        program_counter, acc = execute_line(instruction, operand, program_counter, acc)
    return (False, acc)

def try_mutations(program):
    for i in range(len(program)):
        terminated, final_acc = try_mutation(program, i)
        if terminated:
            return (i, terminated, final_acc)

def try_mutation(program, i):
    (instruction, operand) = program[i]
    mutations = {"nop": "jmp", "jmp": "nop"}
    if instruction in mutations:
        return run_program(program[:i] + [(mutations[instruction], operand)] + program[i+1:])
    else:
        return (False, 0)

f = open('input.txt')
ls = f.readlines()
program = map(parse_line, ls)
print(run_program(program))
print(try_mutations(program))