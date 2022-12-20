import re
import copy

f = open('test_input.txt')
blueprints = []
for line in f:
  ore_ore = int(re.search(r'ore robot costs (\d+) ore', line).group(1))
  cla_ore = int(re.search(r'clay robot costs (\d+) ore', line).group(1))
  obs_ore, obs_cla = map(int, re.search(r'obsidian robot costs (\d+) ore and (\d+) clay', line).groups())
  geo_ore, geo_obs = map(int, re.search(r'geode robot costs (\d+) ore and (\d+) obsidian', line).groups())
  print(f'ore: {ore_ore} ore. clay: {cla_ore} ore. obsidian: {obs_ore} ore, {obs_cla} clay. geode: {geo_ore} ore, {geo_obs} obsidian.')
  blueprint = {'ore': {'ore': ore_ore}, 
               'cla': {'ore': cla_ore}, 
               'obs': {'ore': obs_ore, 'cla': obs_cla}, 
               'geo': {'ore': geo_ore, 'obs': geo_obs}}
  blueprints.append(blueprint)

def can_build(blueprint, stocks, robot):
  for ingredient in blueprint[robot]:
    if stocks[ingredient] < blueprint[robot][ingredient]:
      return False
  return True

def pay_for(blueprint, stocks, robot):
  for ingredient in blueprint[robot]:
    stocks[ingredient] -= blueprint[robot][ingredient]

def add_into_second_dict(d1, d2):
  for k, v in d1.items():
    d2[k] += v

def find_earliest_geo(blueprint, robots_start, stocks_start):
  worlds = [{'robots': copy.copy(robots_start), 'stocks': copy.copy(stocks_start), 't': 0, 'history': []}]
  while not any([world['stocks']['geo'] > 0 for world in worlds]):
    # build new robots
    new_worlds = []
    for world in worlds:
      world['new_robots'] = {'ore': 0, 'cla': 0, 'obs': 0, 'geo': 0}
      for robot in world['robots']:
        if can_build(blueprint, world['stocks'], robot):
          new_world = copy.deepcopy(world)
          new_world['history'].append(f"{robot}{world['t']}")
          pay_for(blueprint, new_world['stocks'], robot)
          new_world['new_robots'][robot] += 1
          new_worlds.append(new_world)

    worlds.extend(new_worlds)

    print(f"t: {worlds[0]['t']}, num worlds: {len(worlds)}")

    # extract resources
    # add new robots
    # increment time
    for world in worlds:
      add_into_second_dict(world['robots'], world['stocks'])
      add_into_second_dict(world['new_robots'], world['robots'])
      world['t'] += 1
    
    worlds = [world for world in worlds if 
              world['stocks']['ore'] < 20
              and world['stocks']['cla'] < 20
              and world['stocks']['obs'] < 20
              ]
  
  return [world for world in worlds if world['stocks']['geo'] > 0]
    
    
robots_start = {'ore': 1, 'cla': 0, 'obs': 0, 'geo': 0}
stocks_start = {'ore': 0, 'cla': 0, 'obs': 0, 'geo': 0}
for blueprint in blueprints:
  print(find_earliest_geo(blueprint, robots_start, stocks_start))
  