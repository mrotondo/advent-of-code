path = File.join(File.dirname(__FILE__), "input.txt")

def first_largest_digit(string)
  (0..9).reverse_each do |i|
    index = string.index(i.to_s)
    if index
      return [i, index]
    end
  end
  [nil, nil]
end

def find_largest_joltage(bank, num_batteries)
  joltage = 0
  (0...num_batteries).reverse_each do |batteries_remaining|
    # don't consider the last n batteries when choosing, since that won't allow enough subsequent batteries to be chosen
    digit, digit_index = first_largest_digit(bank[0..-(1 + batteries_remaining)])
    bank = bank[digit_index + 1..]
    joltage += digit * 10**batteries_remaining
  end
  joltage
end

banks = File.readlines(path, chomp: true)

part_1_joltage_sum = 0
part_2_joltage_sum = 0
banks.each do |bank|
  part_1_joltage_sum += find_largest_joltage(bank, 2)
  part_2_joltage_sum += find_largest_joltage(bank, 12)
end
puts part_1_joltage_sum
puts part_2_joltage_sum