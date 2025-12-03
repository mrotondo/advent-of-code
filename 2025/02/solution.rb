require "benchmark"

path = File.join(File.dirname(__FILE__), "input.txt")

def invalid_id(id, max_repetitions: id.to_s.length)
  repetitions_to_check = (2..max_repetitions)
  id_length = id.to_s.length
  repetitions_to_check.each do |repetition_count|
    next if id_length % repetition_count != 0
    repetition_length = id_length / repetition_count
    all_chunks_match = true
    chunks = id
    chunks_length = Math.log10(chunks).to_i + 1
    (repetition_count - 1).times do
      chunk = chunks / 10 ** (chunks_length - repetition_length)
      if chunk != chunks % 10 ** repetition_length
        all_chunks_match = false
        break
      end
      chunks = chunks % 10 ** (chunks_length - repetition_length)
      chunks_length -= repetition_length
    end
    if all_chunks_match
      return true
    end
  end
  false
end

part_1_invalid_id_sum = 0
part_2_invalid_id_sum = 0
ranges = File.read(path).split(",")
time = Benchmark.measure do
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
end
puts time.real
puts "Part 1: #{part_1_invalid_id_sum}"
puts "Part 2: #{part_2_invalid_id_sum}"