f = open('input.txt')
lines = f.readlines()

def traverse(lines, xStep, yStep):
    x = 0
    numTrees = 0
    for line in lines[::yStep]:
        l = line.strip()
        i = x % len(l)
        if (l[i] is "#"):
            numTrees += 1
        x += xStep
    return numTrees

a1 = traverse(lines, 1, 1)
a2 = traverse(lines, 3, 1)
a3 = traverse(lines, 5, 1)
a4 = traverse(lines, 7, 1)
a5 = traverse(lines, 1, 2)
print(a1 * a2 * a3 * a4 * a5)
