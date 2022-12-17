from copy import copy

class Block:
  def __init__(self, pieces):
    self.pieces = set(pieces)
    self.size = (1 + max([pos[0] for pos in self.pieces]), 
                 1 + max([pos[1] for pos in self.pieces]))
    self.position = (-1, -1)

  def __repr__(self):
    return str(self.size)

  def __copy__(self):
    return Block(self.pieces)

block_0 = Block([(0, 0), (1, 0), (2, 0), (3, 0)])
block_1 = Block([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)])
block_2 = Block([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)])
block_3 = Block([(0, 0), (0, 1), (0, 2), (0, 3)])
block_4 = Block([(0, 0), (1, 0), (0, 1), (1, 1)])

block_templates = [block_0, block_1, block_2, block_3, block_4]

class World:
  def __init__(self):
    self.pieces = set()
    self.max_ys = [0] * 7
  
  # @profile
  def check_block_move(self, block, move):
    for block_piece in block.pieces:
      translated_piece = vec2_add(block_piece, block.position)
      moved_piece = vec2_add(translated_piece, move)
      if moved_piece in self.pieces or moved_piece[0] < 0 or moved_piece[0] >= 7 or moved_piece[1] < 0:
        return False
    return True

  def add_block(self, block):
    for block_piece in block.pieces:
      translated_piece = vec2_add(block_piece, block.position)
      self.pieces.add(translated_piece)
      x, y = translated_piece
      self.max_ys[x] = max(self.max_ys[x], y)
    
    # lowest_max_y = min(self.max_ys)
    # for piece in list(self.pieces):
    #   x, y = piece
    #   if y < lowest_max_y:
    #     self.pieces.remove(piece)

  def __repr__(self):
    y = max(self.max_ys)
    s = ''
    while y >= 0:
      for x in range(7):
        if (x, y) in self.pieces:
          s += '#'
        else:
          s += '.'
      s += '\n'
      y -= 1
    return s

def vec2_add(a, b):
  return (a[0] + b[0], a[1] + b[1])

def drop_blocks(world, jets, max_blocks):
  max_y = 0
  skip_y = 0
  skipped = False
  num_blocks = 0
  jet_i = 0
  block_i = 0
  block_jet_lineups = {}
  while num_blocks < max_blocks:
    if not skipped and (block_i, jet_i) in block_jet_lineups and len(block_jet_lineups[(block_i, jet_i)]) == 2:
      prev_num_blocks, prev_max_y = block_jet_lineups[(block_i, jet_i)][1]
      num_blocks_increment = num_blocks - prev_num_blocks
      max_y_increment = max_y - prev_max_y
      times_to_increment = (max_blocks - num_blocks) // num_blocks_increment
      num_blocks += num_blocks_increment * times_to_increment
      skip_y = times_to_increment * max_y_increment
      skipped = True
    else:
      block_jet_lineups.setdefault((block_i, jet_i), []).append((num_blocks, max_y))

    block = copy(block_templates[block_i])
    block.position = (2, max_y + 3)
    while True:
      # jet
      jet_arrow = jets[jet_i]
      jet_move = (1, 0)
      if jet_arrow == '<':
        jet_move = (-1, 0)
      if world.check_block_move(block, jet_move):
        block.position = vec2_add(block.position, jet_move)
      jet_i = (jet_i + 1) % len(jets)

      # fall
      fall_move = (0, -1)
      if world.check_block_move(block, fall_move):
        block.position = vec2_add(block.position, fall_move)
      else:
        world.add_block(block)
        max_y = max(max_y, block.position[1] + block.size[1])
        break
    num_blocks += 1
    block_i = (block_i + 1) % len(block_templates)
  return max_y + skip_y


f = open('input.txt')
jets = f.readline().strip()
# max_blocks = 2022
max_blocks = 1000000000000
world = World()
max_y = drop_blocks(world, jets, max_blocks)
print(max_y)