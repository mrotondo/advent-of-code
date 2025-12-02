path = File.join(File.dirname(__FILE__), "input.txt")

def parse_instructions(path)
  line_regex = /([LR])(\d*)/
  directions = {"L" => -1, "R" => 1}

  lines = File.readlines(path, chomp: true)
  lines.map do |line|
    direction, amount = line_regex.match(line).captures
    [directions[direction], amount.to_i]
  end
end

crossings = 0
zeros = 0
dial = 50
rotations = parse_instructions(path)
rotations.each do |direction, amount|
  # part 2: turn by 100s until we can't anymore
  remaining_amount = amount
  while remaining_amount > 99
    remaining_amount -= 100
    crossings += 1
  end

  # part 2: do remaining rotation, but only count a crossing if we didn't start at 0
  prev_dial = dial
  dial += direction * remaining_amount
  if dial <= 0 || dial > 99
    if prev_dial != 0
      crossings += 1
    end
    dial %= 100
  end

  # part 1: count up the simple case of landing on zero
  if dial == 0
    zeros += 1
  end
end
puts "part 1: #{zeros}"
puts "part 2: #{crossings}"