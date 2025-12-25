def rect_size(p1, p2)
  ((p1[0] - p2[0]).abs + 1) * ((p1[1] - p2[1]).abs + 1)
end

def biggest_rect(p, positions)
  positions.max { |o1, o2| rect_size(p, o1) <=> rect_size(p, o2) }
end

# assume axis-aligned (p1 and p2 share an x or y coordinate)
def positions_along_line(p1, p2)
  increment = element_normalize(difference(p1, p2))
  position = p1
  positions = []
  loop do
    yield position if block_given?
    positions << position
    break if position == p2

    position = sum(position, increment)
  end
  positions
end

def rect_valid?(p1, p2, column_lookup, row_lookup)
  min_x, max_x = [p1[0], p2[0]].minmax
  min_y, max_y = [p1[1], p2[1]].minmax

  if row_lookup[min_y].any? { |x| (min_x..max_x).include?(x) } ||
    row_lookup[max_y].any? { |x| (min_x..max_x).include?(x) } ||
    column_lookup[min_x].any? { |y| (min_y..max_y).include?(y) } ||
    column_lookup[max_x].any? { |y| (min_y..max_y).include?(y) }
    false
  else
    true
  end
end

def biggest_rect_without_mark(p, positions, column_lookup, row_lookup)
  positions.max do |o1, o2|
    o1_rect_size = rect_valid?(p, o1, column_lookup, row_lookup) ? rect_size(p, o1) : 0
    o2_rect_size = rect_valid?(p, o2, column_lookup, row_lookup) ? rect_size(p, o2) : 0
    o1_rect_size <=> o2_rect_size
  end
end

def difference(v1, v2)
  [v2[0] - v1[0], v2[1] - v1[1]]
end

def sum(v1, v2)
  [v1[0] + v2[0], v1[1] + v2[1]]
end

def element_normalize(v)
  [v[0] <=> 0, v[1] <=> 0]
end

LEFT = -1
LINE = 0
RIGHT = 1

SIDES = {
  [1, 0] => { left: [0, -1], right: [0, 1] },
  [0, -1] => { left: [-1, 0], right: [1, 0] },
  [-1, 0] => { left: [0, 1], right: [0, -1] },
  [0, 1] => { left: [1, 0], right: [-1, 0] }
}.freeze

def draw_line(p1, p2, marked_positions)
  direction = element_normalize(difference(p1, p2))
  positions_along_line(p1, p2) do |position_to_mark|
    marked_positions[position_to_mark] = LINE

    left_side = sum(position_to_mark, SIDES[direction][:left])
    marked_positions[left_side] ||= LEFT

    right_side = sum(position_to_mark, SIDES[direction][:right])
    marked_positions[right_side] ||= RIGHT
  end
end

path = File.join(File.dirname(__FILE__), "input.txt")
lines = File.readlines(path, chomp: true)
positions = lines.map { |line| /(\d*),(\d*)/.match(line).captures.map(&:to_i) }

positions_to_biggest_rect_sizes = positions.to_h { |p| [p, rect_size(p, biggest_rect(p, positions))] }
puts "part 1: #{positions_to_biggest_rect_sizes.values.max}"

marked_positions = {}
positions[0...-1].each_with_index do |p, i|
  p_next = positions[i + 1]
  draw_line(p, p_next, marked_positions)
end
draw_line(positions[-1], positions[0], marked_positions)

left_side_positions = marked_positions.select { |k, v| v == LEFT }
right_side_positions = marked_positions.select { |k, v| v == RIGHT }
outside = left_side_positions.count < right_side_positions.count ? RIGHT : LEFT

outside_positions = marked_positions.select { |k, v| v == outside }.keys

column_lookup = Hash.new { |h, k| h[k] = Set[] }
row_lookup = Hash.new { |h, k| h[k] = Set[] }
outside_positions.each do |o_p|
  x, y = o_p
  column_lookup[x].add(y)
  row_lookup[y].add(x)
end

positions_to_biggest_internal_rects = positions.to_h do |p|
  [p, biggest_rect_without_mark(p, positions, column_lookup, row_lookup)]
end
internal_rect_sizes = positions_to_biggest_internal_rects.map { |p1, p2| rect_size(p1, p2) }

puts "part 2: #{internal_rect_sizes.max}"
