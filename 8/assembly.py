f = open('input.txt')
ls = f.readlines()

def parse_line(l):
    return (l[:3], int(l[4:-1]))

def run_program(ls):
    acc = 0
    executed_lines = set()
    program_counter = 0
    while(program_counter not in executed_lines):
        if program_counter == len(ls):
            return (True, acc)
        elif program_counter > len(ls):
            return (False, acc)
        l = ls[program_counter]
        executed_lines.add(program_counter)
        instruction, operand = parse_line(l)
        if (instruction == "acc"):
            acc += operand
            program_counter += 1
        elif (instruction == "jmp"):
            program_counter += operand
        elif (instruction == "nop"):
            program_counter += 1
    return (False, acc)

def try_mutations(ls):
    for i in range(len(ls)):
        terminated, final_acc = try_mutation(ls, i)
        if terminated:
            return (i, terminated, final_acc)

def try_mutation(ls, i):
    instruction, operand = parse_line(ls[i])
    new_instruction = ""
    if instruction == "acc":
        return (False, 0)
    elif instruction == "jmp":
        new_instruction = "nop"
    elif instruction == "nop":
        new_instruction = "jmp"
    new_line = new_instruction + " " + str(operand) + "\n"
    return run_program(ls[:i] + [new_line] + ls[i+1:])

terminated, final_acc = run_program(ls)
print(final_acc)
print(try_mutations(ls))