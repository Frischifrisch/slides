def stats(*numbers):
   total = 0

   minx = None
   maxx = None

   for val in numbers:
      total += val
      if minx is None:
         minx = maxx = val
      minx = min(minx, val)
      maxx = max(maxx, val)
   average = total / len(numbers) if len(numbers) else None
   return total, average, minx, maxx


ttl, avr, smallest, largest = stats(3, 5, 4)

print(ttl)
print(avr)
print(smallest)
print(largest)

