require 'benchmark'

path = File.join(File.dirname(__FILE__), "input.txt")

def invalid_id(id, max_repetitions: id.length)
  repetitions_to_check = (2..max_repetitions)
  repetitions_to_check.any? do |repetition_count|
    next if id.length % repetition_count != 0
    first_repetition = id[0...id.length / repetition_count]
    id.scan(first_repetition).count == repetition_count
  end
end

part_1_invalid_id_sum = 0
part_2_invalid_id_sum = 0
ranges = File.read(path).split(",")
ranges.each do |range|
  min, max = range.split("-")
  (min.to_i..max.to_i).each do |id|
    if invalid_id(id.to_s, max_repetitions: 2)
      part_1_invalid_id_sum += id
    end
    if invalid_id(id.to_s)
      part_2_invalid_id_sum += id
    end
  end
end
puts "Part 1: #{part_1_invalid_id_sum}"
puts "Part 2: #{part_2_invalid_id_sum}"