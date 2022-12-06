from collections import deque

def find_marker(signal, marker_length):
  window = deque()
  for i, c in enumerate(signal, start=1):
    window.append(c)
    if len(window) > marker_length:
      window.popleft()
      if len(set(window)) == marker_length:
        return i

f = open('input.txt')
signal = f.readline().strip()
print(find_marker(signal, 4))
print(find_marker(signal, 14))