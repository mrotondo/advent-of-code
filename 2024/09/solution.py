f = open('test_input.txt')
line = f.read().strip()

file_sizes = []
space_after_files = []
reading_file = True
for character in line:
  if reading_file:
    file_sizes.append(int(character))
    reading_file = False
  else:
    space_after_files.append(int(character))
    reading_file = True

num_blocks = sum(file_sizes)

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

print(checksum)