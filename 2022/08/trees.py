class Tree:
  def __init__(self, height):
    self.height = height
    self.visible = False
    self.view_score = 0
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
  h = len(trees)
  w = len(trees[0])

  start_height = trees[y][x].height
  view_dist = 0
  while True:
    x += x_inc
    y += y_inc
    if x < 0 or y < 0 or x >= w or y >= h:
      break
    view_dist += 1
    if trees[y][x].height >= start_height:
      break
  return view_dist

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

h = len(trees)
w = len(trees[0])
for y in range(0, h):
  for x in range(0, w):
    up_view = scan(trees, x, y, 0, -1)
    left_view = scan(trees, x, y, -1, 0)
    down_view = scan(trees, x, y, 0, 1)
    right_view = scan(trees, x, y, 1, 0)
    trees[y][x].view_score = up_view * left_view * down_view * right_view

sweep(trees)

num_visible = 0
max_view_score = -1
for row in trees:
  for tree in row:
    if tree.visible:
      num_visible += 1
    if tree.view_score > max_view_score:
      max_view_score = tree.view_score

print(num_visible)
print(max_view_score)