require "benchmark"

path = File.join(File.dirname(__FILE__), "input.txt")

def invalid_id(id)
  id_length = Math.log10(id).to_i + 1
  repetition_count = 1
  while repetition_count <= id_length
    repetition_count += 1
    next if id_length % repetition_count != 0
    repetition_length = id_length / repetition_count
    all_chunks_match = true
    chunks = id
    chunks_length = Math.log10(chunks).to_i + 1
    comparison_chunk = id %  10 ** repetition_length
    chunk_index = 0
    while chunk_index < repetition_count - 1 do
      chunk = chunks / 10 ** (chunks_length - repetition_length)
      if chunk != comparison_chunk
        all_chunks_match = false
        break
      end
      chunks = chunks % 10 ** (chunks_length - repetition_length)
      chunks_length -= repetition_length
      chunk_index += 1
    end
    if all_chunks_match
      return repetition_count
    end
  end
  nil
end

part_1_invalid_id_sum = 0
part_2_invalid_id_sum = 0
ranges = File.read(path).split(",")
time = Benchmark.measure do
  ranges.each do |range|
    min_id, max_id = range.split("-")
    min_id = min_id.to_i
    max_id = max_id.to_i
    id = min_id
    while id <= max_id
      repetitions_found = invalid_id(id)
      if repetitions_found == 2
        part_1_invalid_id_sum += id
      end
      if repetitions_found != nil
        part_2_invalid_id_sum += id
      end
      id += 1
    end
  end
end
puts time.real
puts "Part 1: #{part_1_invalid_id_sum}"
puts "Part 2: #{part_2_invalid_id_sum}"