from collections import defaultdict

words = ['Wombat', 'Rhino', 'Sloth', 'Tarantula', 'Sloth', 'Rhino', 'Sloth']

counter = defaultdict(int)
for word in words:
   counter[word] += 1

print(counter)
for word in counter:
   print(f"{word}:{counter[word]}")

