from collections import Counter

words = ['Wombat', 'Rhino', 'Sloth', 'Tarantula', 'Sloth', 'Rhino', 'Sloth']

cnt = Counter()
for word in words:
   cnt[word] += 1

print(cnt)
for word in cnt:
   print(f"{word}:{cnt[word]}")



