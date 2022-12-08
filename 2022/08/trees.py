class Tree:
  def __init__(self, height):
    self.height = height
    self.visible = False
    self.maxes = {(-1,0): -1, (1,0): -1, (0,-1): -1, (0,1): -1}
    self.max_up = -1
    self.max_left = -1
    self.max_down = -1
    self.max_right = -1
  
  def __str__(self):
    return f'{self.height}'

  def __repr__(self):
    return f'{self.height}'# {self.vis_up} {self.vis_left} {self.vis_down} {self.vis_right}'

def sweep(trees):
  h = len(trees)
  w = len(trees[0])

  # down and to the right
  for y in range(1, h-1):
    for x in range(1, w-1):
      tree = trees[y][x]
      left_tree = trees[y][x-1]
      up_tree = trees[y-1][x]

      if tree.height > left_tree.max_left:
        tree.visible = True
      tree.max_left = max(tree.height, left_tree.max_left)

      if tree.height > up_tree.max_up:
        tree.visible = True
      tree.max_up = max(tree.height, up_tree.max_up)

  # up and to the left
  for y in range(h-2, 0, -1):
    for x in range(w-2, 0, -1):
      tree = trees[y][x]
      right_tree = trees[y][x+1]
      down_tree = trees[y+1][x]

      if tree.height > right_tree.max_right:
        tree.visible = True
      tree.max_right = max(tree.height, right_tree.max_right)

      if tree.height > down_tree.max_down:
        tree.visible = True
      tree.max_down = max(tree.height, down_tree.max_down)

def scan(trees, x, y, x_inc, y_inc):
  tree = trees[y][x]
  prev_tree = trees[x-x_inc][y-y_inc]
  prev_tree_max = prev_tree.maxes[(-x_inc, -y_inc)]
  if tree.height > prev_tree_max:
    tree.visible = True
  tree.maxes[(-x_inc, -y_inc)] = max(tree.height)

lines = open('input.txt').readlines()
trees = [list(map(Tree, list(map(int, line.strip())))) for line in lines]

# set outer ring
for tree in trees[0]:
  tree.max_up = tree.height
  tree.visible = True
for tree in trees[-1]:
  tree.max_down = tree.height
  tree.visible = True
for row in trees:
  left_tree = row[0]
  left_tree.max_left = left_tree.height
  left_tree.visible = True
  
  right_tree = row[-1]
  right_tree.max_right = right_tree.height
  right_tree.visible = True

sweep(trees)

num_visible = 0
for row in trees:
  for tree in row:
    if tree.visible:
      num_visible += 1

print(num_visible)