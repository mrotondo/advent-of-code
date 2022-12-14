import ast
from enum import Enum


class Packet:
    def __init__(self, list):
        self.list = list

    def __getitem__(self, key):
        return self.list[key]

    def __len__(self):
        return len(self.list)

    def __eq__(self, other):
        return compare(self, other) == 0

    def __ne__(self, other):
        return compare(self, other) != 0

    def __lt__(self, other):
        return compare(self, other) < 0

    def __repr__(self):
        return str(self.list)

    def pop(self, index):
        return self.list.pop(index)


def compare(left, right):
    i = 0
    while i < len(left) and i < len(right):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return -1  # correct
            elif left[i] > right[i]:
                return 1  # incorrect
        elif isinstance(left[i], list) and isinstance(right[i], list):
            sublist_comparison = compare(left[i], right[i])
            if sublist_comparison != 0:
                return sublist_comparison
        else:
            if isinstance(left[i], int):
                sublist_comparison = compare([left[i]], right[i])
                if sublist_comparison != 0:
                    return sublist_comparison
            elif isinstance(right[i], int):
                sublist_comparison = compare(left[i], [right[i]])
                if sublist_comparison != 0:
                    return sublist_comparison
        i += 1
    if len(left) > i:
        return 1  # incorrect
    elif len(left) == i and len(right) == i:
        return 0
    else:
        return -1


f = open("input.txt")

lines = f.readlines()
lists = map(ast.literal_eval, map(
    str.strip, [line for line in lines if line != "\n"]))
packets = list(map(Packet, lists))
pairs = zip(packets[::2], packets[1::2])
results = list(map(lambda pair: compare(pair[0], pair[1]), pairs))
correct_indices = [
    i + 1 for i in range(len(results)) if results[i] == -1 or results[i] == 0
]

print(sum(correct_indices))

divider_packet_1 = Packet([[2]])
divider_packet_2 = Packet([[6]])
packets.append(divider_packet_1)
packets.append(divider_packet_2)
ordered_packets = sorted(packets)
print((ordered_packets.index(divider_packet_1) + 1)
      * (ordered_packets.index(divider_packet_2) + 1))
