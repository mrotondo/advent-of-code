def sqr_dist(v1, v2)
  (v1[0] - v2[0])**2 + (v1[1] - v2[1])**2 + (v1[2] - v2[2])**2
end

def connect(p1, p2, connections)
  return false if connections[p1]&.include?(p2)

  connections[p1].add(p2)
  connections[p2].add(p1)
  true
end

def circuit(p, connections, circuit_so_far = Set[])
  return circuit_so_far if circuit_so_far.include?(p)

  reachable = Set[]
  connections[p].each do |connection|
    reachable += circuit(connection, connections, circuit_so_far + Set[p])
  end
  circuit_so_far + Set[p] + reachable
end

path = File.join(File.dirname(__FILE__), "input.txt")
lines = File.readlines(path, chomp: true)

positions = lines.map { |line| /(\d*),(\d*),(\d*)/.match(line).captures.map(&:to_i) }

pairs = positions.flat_map do |p1|
  other_positions = positions.reject { |p2| p2 == p1 }
  other_positions.map do |p2|
    [p1, p2, sqr_dist(p1, p2)]
  end
end

sorted_pairs = pairs.sort do |pair1, pair2|
  pair1[2] <=> pair2[2]
end

connections = Hash.new { |h, k| h[k] = Set.new }

sorted_pairs.each do |pair|
  p1, p2, _d = pair
  connect(p1, p2, connections)

  if positions.all? { |p| connections.include?(p) }
    puts p1[0] * p2[0]
    break
  end
end
#
# circuits = Set[]
# boxes_to_circuits.each_value do |c|
#   circuits.add(c)
# end
#
# circuit_sizes = circuits.map(&:size)
# puts circuit_sizes.sort.reverse.first(3).reduce(&:*)
