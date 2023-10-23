p1 = (2, 3)

points = {p1: 'Joe'}
points[(17, 5)] = 'Jane'

print(points)
for k, v in points.items():
   print(k)
   print(k.__class__.__name__)
   print(v)
