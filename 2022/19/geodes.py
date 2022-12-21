import re
import copy
import sys

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

def find_earliest_geo(blueprint):
  robots_start = {'ore': 1, 'cla': 0, 'obs': 0, 'geo': 0}
  stocks_start = {'ore': 0, 'cla': 0, 'obs': 0, 'geo': 0}
  worlds = [{'robots': robots_start, 'stocks': stocks_start, 't': 0, 'history': []}]
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

def run_greedy(blueprint):
  robots = {'ore': 1, 'cla': 0, 'obs': 0, 'geo': 0}
  stocks = {'ore': 0, 'cla': 0, 'obs': 0, 'geo': 0}
  for t in range(24):
    print(t)
    for robot in ['geo', 'obs', 'cla', 'ore']:
      if can_build(blueprint, stocks, robot):
        build(blueprint, robots, stocks, robot)
        break
    add_into_second_dict(robots, stocks)
  print(robots)
  print(stocks)
  return stocks['geo']

def run_ratio(blueprint):
  robots = {'ore': 1, 'cla': 0, 'obs': 0, 'geo': 0}
  stocks = {'ore': 0, 'cla': 0, 'obs': 0, 'geo': 0}
  for t in range(1, 25):
    new_robots = {'ore': 0, 'cla': 0, 'obs': 0, 'geo': 0}
    
    geo_ratio_goal = blueprint['geo']['ore'] / blueprint['geo']['obs']
    geo_ratio_prod = robots['ore'] / robots['obs'] if robots['obs'] > 0 else sys.maxsize

    obs_ratio_goal = blueprint['obs']['ore'] / blueprint['obs']['cla']
    obs_ratio_prod = robots['ore'] / robots['cla'] if robots['cla'] > 0 else sys.maxsize

    if can_build(blueprint, stocks, 'geo'):
      print(f't: {t}, building a geode robot')
      pay_for(blueprint, stocks, 'geo')
      new_robots['geo'] = 1
    elif geo_ratio_prod > geo_ratio_goal and can_build(blueprint, stocks, 'obs'):
      print(f't: {t}, building an obsidian robot')
      pay_for(blueprint, stocks, 'obs')
      new_robots['obs'] = 1
    elif obs_ratio_prod > obs_ratio_goal and can_build(blueprint, stocks, 'cla'):
      print(f't: {t}, building a clay robot')
      pay_for(blueprint, stocks, 'cla')
      new_robots['cla'] = 1
    elif can_build(blueprint, stocks, 'ore'):
      print(f't: {t}, building an ore robot')
      pay_for(blueprint, stocks, 'ore')
      new_robots['ore'] = 1
    add_into_second_dict(robots, stocks)
    add_into_second_dict(new_robots, robots)
    print(f'end of t: {t}, stocks: {stocks}')

  print(f'robots: {robots}')
  print(f'stocks: {stocks}')
  return stocks['geo']

def run_quota(blueprint):
  robots = {'ore': 1, 'cla': 0, 'obs': 0, 'geo': 0}
  stocks = {'ore': 0, 'cla': 0, 'obs': 0, 'geo': 0}
  obs_needed_for_one_geo = blueprint['geo']['obs']
  cla_needed_for_one_geo = blueprint['obs']['cla'] * blueprint['geo']['obs']
  ore_needed_for_one_geo = blueprint['geo']['ore'] + blueprint['geo']['obs'] * blueprint['obs']['ore'] + blueprint['obs']['cla'] * blueprint['cla']['ore']

  norm_denominator = min([obs_needed_for_one_geo, cla_needed_for_one_geo, ore_needed_for_one_geo])
  obs_needed_for_one_geo /= norm_denominator
  cla_needed_for_one_geo /= norm_denominator
  ore_needed_for_one_geo /= norm_denominator

  print(f'obs_needed_for_one_geo: {obs_needed_for_one_geo}')
  print(f'cla_needed_for_one_geo: {cla_needed_for_one_geo}')
  print(f'ore_needed_for_one_geo: {ore_needed_for_one_geo}')
  for t in range(1, 25):
    print(f'starting t {t} ------------')
    new_robots = {'ore': 0, 'cla': 0, 'obs': 0, 'geo': 0}
    
    needed = {
      'obs': obs_needed_for_one_geo - (robots['obs'] % obs_needed_for_one_geo),
      'cla': cla_needed_for_one_geo - (robots['cla'] % cla_needed_for_one_geo),
      'ore': ore_needed_for_one_geo - (robots['ore'] % ore_needed_for_one_geo),
    }
    print(f'needed: {needed}')
    satisfaction_levels = {
      'obs': robots['obs'] // obs_needed_for_one_geo,
      'cla': robots['cla'] // cla_needed_for_one_geo,
      'ore': robots['ore'] // ore_needed_for_one_geo,
      }
    print(f'satisfaction levels: {satisfaction_levels}')
    max_satisfaction_level = max(satisfaction_levels.values())
    print(f'max satisfaction level: {max_satisfaction_level}')
    needed = {k:v for k,v in needed.items() if satisfaction_levels[k] <= max_satisfaction_level}
    print(f'filtered needed: {needed}')

    next_robot = max(needed, key=needed.get)

    print(f't: {t}, next robot: {next_robot}')

    if can_build(blueprint, stocks, 'geo'):
      print(f't: {t}, building a geode robot')
      pay_for(blueprint, stocks, 'geo')
      new_robots['geo'] += 1
    if can_build(blueprint, stocks, next_robot):
      print(f't: {t}, building a {next_robot} robot')
      pay_for(blueprint, stocks, next_robot)
      new_robots[next_robot] += 1
    add_into_second_dict(robots, stocks)
    add_into_second_dict(new_robots, robots)
    print(f'end of t: {t}, stocks: {stocks}')

  print(f'robots: {robots}')
  print(f'stocks: {stocks}')
  return stocks['geo']

def run_priority(blueprint):
  print(f'===============')
  print(f'running priority with blueprint {blueprint}')
  robots = {'ore': 1, 'cla': 0, 'obs': 0, 'geo': 0}
  stocks = {'ore': 0, 'cla': 0, 'obs': 0, 'geo': 0}
  for t in range(1, 25):
    print(f't is {t}')
    new_robots = {'ore': 0, 'cla': 0, 'obs': 0, 'geo': 0}
    # decide
    priority = None # wait by default
    if can_build(blueprint, stocks, 'geo'):
      priority = 'geo'
    else:
      # can't afford geode robot
      geo_ore_prod_to_cost_ratio = robots['ore'] / blueprint['geo']['ore']
      geo_obs_prod_to_cost_ratio = (robots['obs'] + 1) / blueprint['geo']['obs']
      print(f'comparing geo_ore_prod_to_cost_ratio {geo_ore_prod_to_cost_ratio} to geo_obs_prod_to_cost_ratio {geo_obs_prod_to_cost_ratio}')
      if geo_ore_prod_to_cost_ratio <= geo_obs_prod_to_cost_ratio:
        priority = 'ore'
      else:
        priority = 'obs'  # we're not producing enough obsidian to build geode robots
        if not can_build(blueprint, stocks, 'obs'):
          obs_ore_prod_to_cost_ratio = robots['ore'] / blueprint['obs']['ore']
          obs_cla_prod_to_cost_ratio = (robots['cla'] + 1) / blueprint['obs']['cla']
          print(f'comparing obs_ore_prod_to_cost_ratio {obs_ore_prod_to_cost_ratio} to {obs_cla_prod_to_cost_ratio}')
          if obs_ore_prod_to_cost_ratio <= obs_cla_prod_to_cost_ratio:
            priority = None #'ore'
          else:
            priority = 'cla'  # we're not producing enough clay to build obsidian robots
      
    # pay for & start building robots
    print(f'priority is {priority}')
    if priority and can_build(blueprint, stocks, priority):
      print(f'start of t: {t}, building {priority}')
      pay_for(blueprint, stocks, priority)
      new_robots[priority] = 1

    # robots extract
    add_into_second_dict(robots, stocks)

    # finish building robots
    add_into_second_dict(new_robots, robots)
    
    print(f'end of t: {t}, robots: {robots}, stocks: {stocks}')
    print(f'----')

  return stocks['geo']


for i, blueprint in enumerate(blueprints):
  # print(find_earliest_geo(blueprint))
  # print((i + 1) * run_ratio(blueprint))
  # print((i + 1) * run_quota(blueprint))
  print((i + 1) * run_priority(blueprint))