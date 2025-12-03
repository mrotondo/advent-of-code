path = File.join(File.dirname(__FILE__), "input.txt")

def invalid_id(id, max_repetitions: id.to_s.length)
  repetitions_to_check = (2..max_repetitions)
  id_length = id.to_s.length
  repetitions_to_check.any? do |repetition_count|
    next if id_length % repetition_count != 0
    repetition_length = id_length / repetition_count
    first_chunk = id / 10 ** (id_length - repetition_length)
    (0...repetition_count - 1).all? do |repetition_index|
      chunk = id % 10 ** (repetition_length * (repetition_index + 1)) / 10 ** (repetition_length * repetition_index)
      chunk == first_chunk
    end
  end
end

part_1_invalid_id_sum = 0
part_2_invalid_id_sum = 0
ranges = File.read(path).split(",")
ranges.each do |range|
  min, max = range.split("-")
  (min.to_i..max.to_i).each do |id|
    if invalid_id(id, max_repetitions: 2)
      part_1_invalid_id_sum += id
    end
    if invalid_id(id)
      part_2_invalid_id_sum += id
    end
  end
end
puts "Part 1: #{part_1_invalid_id_sum}"
puts "Part 2: #{part_2_invalid_id_sum}"