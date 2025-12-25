def load_machines(lines)
  goal_regex = /[.#]+/
  transition_regex = /\([\d,]+\)/
  joltage_requirements_regex = /\{(?:\d+,?)+\}/

  lines.map do |line|
    goal = goal_regex.match(line)[0].split("")

    transitions = line.scan(transition_regex)
    transitions = transitions.map do |transition|
      Set.new(transition.gsub(/[()]/, "").split(",").map(&:to_i))
    end

    joltage_requirements = joltage_requirements_regex.match(line)[0]
    joltage_requirements = joltage_requirements.gsub(/[{}]/, "").split(",").map(&:to_i)

    { goal:, transitions:, joltage_requirements: }
  end
end

def initial_lights(machine)
  ["."] * machine[:goal].length
end

def initial_joltages(machine)
  [0] * machine[:goal].length
end

LIGHT_TOGGLE = { "." => "#", "#" => "." }

def apply_lights_transition(lights, transition)
  lights.each_with_index.map do |light, i|
    if transition.include? i
      LIGHT_TOGGLE[light]
    else
      light
    end
  end
end

def apply_joltages_transition(joltages, transition)
  joltages.each_with_index.map do |joltage, i|
    if transition.include? i
      joltage + 1
    else
      joltage
    end
  end
end

def joltages_state_disqualifier(joltages, joltage_requirements)
  joltages.each_with_index.any? { |joltage, i| joltage > joltage_requirements[i] }
end

def find_path_length_to_goal(initial_state, goal_state, transitions, transition_applier, state_disqualifier = nil)
  num_presses = 0
  visited_states = Set[]
  current_states = Set[initial_state]
  loop do
    num_presses += 1
    new_states = Set[]
    current_states.each do |current_state|
      transitions.each do |transition|
        new_state = transition_applier.call(current_state, transition)
        return num_presses if new_state == goal_state

        next if state_disqualifier&.call(new_state, goal_state)

        unless visited_states.include?(new_state)
          visited_states.add(new_state)
          new_states.add(new_state)
        end
      end
    end
    current_states = new_states
  end
end

path = File.join(File.dirname(__FILE__), "input.txt")
lines = File.readlines(path, chomp: true)

machines = load_machines(lines)

lights_presses = machines.sum do |machine|
  find_path_length_to_goal(
    initial_lights(machine),
    machine[:goal],
    machine[:transitions],
    method(:apply_lights_transition)
  )
end
puts "part 1: #{lights_presses}"

joltages_presses = machines.sum do |machine|
  find_path_length_to_goal(
    initial_joltages(machine),
    machine[:joltage_requirements],
    machine[:transitions],
    method(:apply_joltages_transition),
    method(:joltages_state_disqualifier)
  )
end
puts "part 2: #{joltages_presses}"
