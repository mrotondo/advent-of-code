require "set"

path = File.join(File.dirname(__FILE__), "input.txt")
lines = File.readlines(path, chomp: true)

SOURCE = "S"
SPLITTER = "^"

source_position = [lines[0].index(SOURCE), 0]
splitter_positions = lines.each_with_index.flat_map do |line, y|
  line
    .split("")
    .each_with_index
    .select { |c, x| c == SPLITTER }
    .map { |c, x| [x, y] }
end
splitter_hit_counts = splitter_positions.to_h { |pos| [pos, 0] }

top_splitter_pos = splitter_hit_counts
                     .keys
                     .select { |pos| pos[0] == source_position[0] }
                     .min { |pos| pos[1] }
splitter_hit_counts[top_splitter_pos] = 1

num_beams_hitting_bottom = 0

def cast_beam(x_check, start_y, max_y, source_splitter_count, splitter_hit_counts)
  num_beams_hitting_bottom = 0
  hit = false
  (start_y..max_y).each do |y_check|
    left_hit_splitter = splitter_hit_counts.select { |pos, count| pos == [x_check, y_check] }.first
    if left_hit_splitter
      splitter_hit_counts[left_hit_splitter[0]] += source_splitter_count
      hit = true
      break
    end
  end
  unless hit
    num_beams_hitting_bottom += source_splitter_count
  end
  num_beams_hitting_bottom
end

(top_splitter_pos[1]..lines.length).each do |y_source|
  source_splitters = splitter_hit_counts.select { |pos, _| pos[1] == y_source }
  source_splitters.each do |source_splitter_pos, source_splitter_count|
    # cast left
    num_beams_hitting_bottom += cast_beam(
      source_splitter_pos[0] - 1,
      source_splitter_pos[1] + 1,
      lines.length,
      source_splitter_count,
      splitter_hit_counts
    )

    # cast right
    num_beams_hitting_bottom += cast_beam(
      source_splitter_pos[0] + 1,
      source_splitter_pos[1] + 1,
      lines.length,
      source_splitter_count,
      splitter_hit_counts
    )
  end
end

puts "part 1: #{splitter_hit_counts.select { |_, count| count > 0 }.count}"
puts "part 2: #{num_beams_hitting_bottom}"
