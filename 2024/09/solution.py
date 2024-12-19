input_file = open('input.txt')
disk = input_file.read().strip()

def read_disk(disk):
  file_sizes = {}
  space_after_files = {}
  reading_file = True
  file_id = 0
  for character in disk:
    if reading_file:
      file_sizes[file_id] = int(character)
      reading_file = False
    else:
      space_after_files[file_id] = int(character)
      reading_file = True
      file_id += 1
  return file_sizes, space_after_files

def compact_files(file_sizes, space_after_files):
  num_blocks = sum(file_sizes.values())
  next_original_file_id = 0
  space_left_to_fill = 0
  blocks_filled = 0
  checksum = 0
  while blocks_filled < num_blocks:
    if space_left_to_fill == 0:
      for block_position in range(blocks_filled, blocks_filled + file_sizes[next_original_file_id]):
        checksum += block_position * next_original_file_id
      blocks_filled += file_sizes[next_original_file_id]
      space_left_to_fill = min(space_after_files[next_original_file_id], num_blocks - blocks_filled)
      next_original_file_id += 1
    else:
      while space_left_to_fill > 0:
        last_file_id = len(file_sizes) - 1
        blocks_fillable_from_last_file = min(space_left_to_fill, file_sizes[last_file_id])
        for block_position in range(blocks_filled, blocks_filled + blocks_fillable_from_last_file):
          checksum += block_position * last_file_id
        file_sizes[last_file_id] -= blocks_fillable_from_last_file
        if file_sizes[last_file_id] == 0:
          del(file_sizes[last_file_id])
        space_left_to_fill -= blocks_fillable_from_last_file
        blocks_filled += blocks_fillable_from_last_file
  return checksum

file_sizes, space_after_files = read_disk(disk)
print(compact_files(file_sizes, space_after_files))

class File:
  def __init__(self, id, size, l_space):
    self.id = id
    self.size = size
    self.l_space = l_space
    self.r_space = None
    if l_space:
      l_space.r_file = self

  def __repr__(self):
    return "{}: {}".format(self.id, self.size)
  
  def l_file(self):
    if self.l_space:
      return self.l_space.l_file

  def r_file(self):
    if self.r_space:
      return self.r_space.r_file

  def last_file(self):
    file = self
    while file.r_space:
      file = file.r_file()
    return file

  def move_right_of_file(self, l_file):
    if self.r_space:
      self.l_space.size += self.size
      self.l_space.merge_with_right_space(self.r_space)
    else:
      self.l_file().r_space = None

    self.r_space = l_file.r_space
    if self.r_space:
      self.r_space.l_file = self
      self.r_space.size -= self.size

    self.l_space = Space(0, l_file)
    self.l_space.r_file = self

class Space:
  def __init__(self, size, l_file):
    self.size = size
    self.l_file = l_file
    self.r_file = None
    l_file.r_space = self
  
  def merge_with_right_space(self, r_space):
    if r_space:
      self.size += r_space.size
      self.r_file = r_space.r_file
      self.r_file.l_space = self
    else:
      self.r_file = None
  
def create_files_and_spaces(file_sizes, space_after_files):
  first_file = File(0, file_sizes[0], None)

  prev_file = first_file
  for file_id in sorted(file_sizes.keys())[1:]:
    l_space = Space(space_after_files[file_id - 1], prev_file)
    prev_file = File(file_id, file_sizes[file_id], l_space)
  
  return first_file, prev_file

file_sizes, space_after_files = read_disk(disk)
first_file, last_file = create_files_and_spaces(file_sizes, space_after_files)

file_to_move = last_file
while file_to_move.l_space:
  next_file_to_move = file_to_move.l_file()
  candidate_file_to_insert_after = first_file
  while candidate_file_to_insert_after != file_to_move:
    if file_to_move.size <= candidate_file_to_insert_after.r_space.size:
      file_to_move.move_right_of_file(candidate_file_to_insert_after)
      break
    candidate_file_to_insert_after = candidate_file_to_insert_after.r_file()
  file_to_move = next_file_to_move

f = first_file
i = 0
total = 0
while(f):
  #print(str(f.id) * f.size, end="")
  for j in range(f.size):
    #print("adding i {} * id {}".format(i, f.id))
    total += i * f.id
    i += 1
  
  if f.r_space:
    #print("." * f.r_space.size, end="")
    i += f.r_space.size

  f = f.r_file()
print(total)