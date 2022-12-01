import re

def find_all_containing(bag, all_contained_by, containers_so_far):
    containers = set(all_contained_by[bag])
    new_containers_so_far = set.union(containers_so_far, containers)
    recursive_containers = []
    for container in containers:
        if container not in containers_so_far:
            recursive_containers.append(find_all_containing(container, all_contained_by, new_containers_so_far))
    return set.union(containers, *recursive_containers)

def find_num_contents(bag, all_bag_contents):
    total_bags = 0
    for (contained_bag, num) in all_bag_contents[bag].items():
        total_bags += num + num * find_num_contents(contained_bag, all_bag_contents)
    return total_bags

f = open('input.txt')
ls = f.readlines()

bag_re = re.compile(r"(.*) bags contains (?:(\d*) (.*) bag.*?)+")
bag_contents = {}
contained_by = {}
for l in ls:
    bag = re.search(r"(.*) bags contain", l).groups()[0]
    contains = re.findall(r"(\d+) (.*?) bag", l)
    contents = {}
    contained_by.setdefault(bag, set())
    for (num, contained_bag) in contains:
        contents[contained_bag] = int(num)
        contained_by.setdefault(contained_bag, set()).add(bag)
    bag_contents[bag] = contents

shiny_gold_containers = find_all_containing("shiny gold", contained_by, set())
print(len(shiny_gold_containers))
print(find_num_contents("shiny gold", bag_contents))