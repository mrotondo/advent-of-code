path = File.join(File.dirname(__FILE__), "input.txt")
lines = File.readlines(path, chomp: true)

PAPER = "@"
FLOOR = "."

grid = {}
lines.each_with_index do |line, y|
  line.split("").each_with_index do |char, x|
    grid[[x, y]] = char
  end
end

def neighbors(grid, pos)
  x, y = pos
  (-1..1).flat_map do |x_offset|
    (-1..1).map do |y_offset|
      next if x_offset == 0 && y_offset == 0
      neighbor_pos = [x + x_offset, y + y_offset]
      [neighbor_pos, grid[neighbor_pos]]
    end
  end
end

def accessible_rolls(grid)
  grid.select do |pos, item|
    if item == PAPER
      num_neighboring_rolls = neighbors(grid, pos).count do |_neighbor_pos, neighbor_item|
        neighbor_item == PAPER
      end
      num_neighboring_rolls < 4
    end
  end
end

puts "part 1: #{accessible_rolls(grid).count}"

num_rolls_removed = 0
loop do
  rolls_to_remove = accessible_rolls(grid)
  break if rolls_to_remove.count == 0
  num_rolls_removed += rolls_to_remove.count
  rolls_to_remove.each do |pos, _item|
    grid[pos] = FLOOR
  end
end

puts "part 2: #{num_rolls_removed}"