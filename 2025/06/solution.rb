path = File.join(File.dirname(__FILE__), "input.txt")
lines = File.readlines(path, chomp: true)

rows = lines.map { |line| line.split(" ")}
columns = rows[0].count.times.map do |column_i|
  rows.count.times.map do |row_i|
    rows[row_i][column_i]
  end
end

def apply_operator(operator, numbers)
  case operator
  when "+"
    numbers.sum
  when "*"
    numbers.reduce(1) { |acc, number| acc * number }
  else
    0
  end
end

grand_total = columns.sum do |column|
  numbers = column[0...-1].map(&:to_i)
  operator = column[-1]
  apply_operator(operator, numbers)
end

puts "part 1: #{grand_total}"

operators_with_indexes = lines[-1].split("").each_with_index.select do |char, index|
  char != " "
end

def vertical_numbers(rows)
  number_count = rows[0].length
  (0...number_count).map do |num_i|
    rows.map { |row_i| row_i[num_i] }.join("").to_i
  end
end

part_2_grand_total = operators_with_indexes[0..-1].each_with_index.sum do |operator_with_index, i|
  operator, operator_index = operator_with_index
  _, next_operator_index = operators_with_indexes[i+1] || [nil, lines[0].length + 2]
  rows = lines[0...-1].map { |line| line[operator_index...next_operator_index-1]}
  apply_operator(operator, vertical_numbers(rows))
end

puts "part 2: #{part_2_grand_total}"