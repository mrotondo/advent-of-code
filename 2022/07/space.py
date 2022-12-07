import re

class EnumWithCurrent:
  def __init__(self, enum):
    self.enum = enum
    self.curr = None

  def next(self):
    try:
      self.curr = next(self.enum)
    except StopIteration:
      self.curr = None
    return self.curr

  def current(self):
    return self.curr

cd_out = re.compile(r'\$ cd \.\.')
cd_in = re.compile(r'\$ cd ([a-z\/]+)')
ls = re.compile(r'\$ ls')
dir_entry = re.compile(r'dir ([a-z]+)')
file_entry = re.compile(r'(\d+) ([a-z\.]+)')

def new_dir():
  return {'dirs': {}, 'files': {}}

def parse_cmd_list(cmd_list, tree):
  while cmd := cmd_list.current():
    if ls.search(cmd):
      cmd_list.next()
      parse_ls(cmd_list, tree)
    elif match := cd_in.search(cmd):
      cmd_list.next()
      parse_cmd_list(cmd_list, tree['dirs'][match.group(1)])
    elif cd_out.search(cmd):
      cmd_list.next()
      return

def parse_ls(cmd_list, tree):
  while cmd := cmd_list.current():
    if match := dir_entry.search(cmd):
      dir_name = match.group(1)
      tree['dirs'][dir_name] = new_dir()
    elif match := file_entry.search(cmd):
      file_size, file_name = match.groups()
      tree['files'][file_name] = int(file_size)
    else:
      return
    cmd_list.next()

def calc_sizes(tree, all_dirs):
  total_size = 0
  for file_name, file_size in tree['files'].items():
    total_size += file_size
  for dir_name, dir_tree in tree['dirs'].items():
    dir_size = calc_sizes(dir_tree, all_dirs)
    all_dirs.append(dir_size)
    total_size += dir_size
  return total_size

cmd_list = EnumWithCurrent(open('input.txt'))
cmd_list.next(); cmd_list.next()  # skip cd /
tree = new_dir()
parse_cmd_list(cmd_list, tree)

dirs_total_sizes = []
total_size = calc_sizes(tree, dirs_total_sizes)
dirs_total_sizes.append(total_size)

at_most_100_k = [size for size in dirs_total_sizes if size <= 100_000]
print(sum(at_most_100_k))

needed_deletion = total_size - 40_000_000
sufficient_dirs = [size for size in dirs_total_sizes if size >= needed_deletion]
print(sorted(sufficient_dirs)[0])