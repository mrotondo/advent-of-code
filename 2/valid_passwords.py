import re

def check_password_1(rule_num_occurrence_range, rule_letter, password):
    return password.count(rule_letter) in rule_num_occurrence_range

def check_password_2(rule_i1, rule_i2, rule_letter, password):
    return (password[rule_i1] == rule_letter) ^ (password[rule_i2] == rule_letter)

f = open('input.txt')
lines = f.readlines()
line_regex = re.compile(r"(\d*)-(\d*) ([a-z]): ([a-z]*)")

num_good_1 = 0
num_good_2 = 0
for line in lines:
    groups = line_regex.match(line).groups()
    rule_i1 = int(groups[0])
    rule_i2 = int(groups[1])
    rule_letter = groups[2]
    password = groups[3]
    if check_password_1(range(rule_i1, rule_i2 + 1), rule_letter, password):
        num_good_1 += 1
    if check_password_2(rule_i1 - 1, rule_i2 - 1, rule_letter, password):
        num_good_2 += 1
print(num_good_1)
print(num_good_2)