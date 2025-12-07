path = File.join(File.dirname(__FILE__), "input.txt")
lines = File.readlines(path, chomp: true)

ranges = []
ids = []
lines.each do |line|
  if line.include? "-"
    min, max = line.split("-")
    ranges.append(Range.new(min.to_i, max.to_i))
  else
    ids.append(line.to_i)
  end
end

num_fresh_ids = ids.count do |id|
  ranges.any? do |range|
    range.include? id
  end
end
puts "part 1: #{num_fresh_ids}"

def ranges_intersect(r1, r2)
  return false if r1 == r2
  (r1.min <= r2.min && r1.max >= r2.min) || (r2.min <= r1.min && r2.max >= r1.max)
end

def range_contains(r1, r2)
  r1.min <= r2.min && r1.max >= r2.max
end

def union_of_intersecting_ranges(r1, r2)
  Range.new([r1.min, r2.min].min, [r1.max, r2.max].max)
end

unioned_ranges = ranges
while unioned_ranges.any? { |r1| unioned_ranges.any? { |r2| ranges_intersect(r1, r2) } }
  new_unioned_ranges = []
  unioned_ranges.each do |range_to_add|
    # skip this if it is fully contained by any in our new list
    if new_unioned_ranges.any? { |already_added_range| range_contains(already_added_range, range_to_add) }
      next
    end

    unioned_ranges.each do |other_range_to_add|
      if ranges_intersect(range_to_add, other_range_to_add)
        range_to_add = union_of_intersecting_ranges(range_to_add, other_range_to_add)
      end
    end

    new_unioned_ranges.append(range_to_add)
  end
  unioned_ranges = new_unioned_ranges
end

puts "part 2: #{unioned_ranges}"
puts "part 2: #{unioned_ranges.sum { |range| range.size }}"