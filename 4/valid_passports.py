import re

def check_passport1(passport):
    return ("byr" in passport and
            "iyr" in passport and
            "eyr" in passport and
            "hgt" in passport and
            "hcl" in passport and
            "ecl" in passport and
            "pid" in passport)

def check_passport2(passport):
    if (not check_passport1(passport)):
        return False
    d = dict(re.findall(r"(\S*):(\S*)", passport))
    byr = int(d["byr"])
    if (byr < 1920 or byr > 2002):
        return False
    iyr = int(d["iyr"])
    if (iyr < 2010 or iyr > 2020):
        return False
    eyr = int(d["eyr"])
    if (eyr < 2020 or eyr > 2030):
        return False
    hgt = int(re.match(r"^(\d*)", d["hgt"]).groups()[0])
    hgt_u_match = re.match(r"\d*([a-z]+)$", d["hgt"])
    if (not hgt_u_match):
        return False
    hgt_u = hgt_u_match.groups()[0]
    if (hgt_u == "cm"):
        if (hgt < 150 or hgt > 193):
            return False
    elif (hgt_u == "in"):
        if (hgt < 59 or hgt > 76):
            return False
    else:
        print(hgt_u)
        return False
    if (not re.match(r"^#[0-9a-f]{6}$", d["hcl"])):
        return False
    if (d["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        return False
    if (not re.match(r"^[0-9]{9}$", d["pid"])):
        return False
    return True

f = open('input.txt')
s = f.read()
passport_re = re.compile(r".*?\n\n", re.DOTALL)
passports = re.findall(passport_re, s)
print(len(passports))
num_valid = 0
for passport in passports:
    if (check_passport2(passport)):
        num_valid += 1
print(num_valid)
