planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']

print(planets)            # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
print(len(planets))       # 6
print(type(planets))      # <class 'list'>

print(planets[0])         # Mercury
print(type(planets[0]))   # <class 'str'>
print(planets[3])         # Mars

print(planets[:2])
print(planets[1:4])       # ['Venus', 'Earth', 'Mars']

print(planets[:1])
print(type(planets[:1]))

print(planets[2:])        # ['Earth', 'Mars', 'Jupiter', 'Saturn']
print(planets[:3])        # ['Mercury', 'Venus', 'Earth']

print(planets[:])         # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
