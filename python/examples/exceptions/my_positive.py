class MyValueError(ValueError):
   def __init__(self, val):
       self.value = val

class MyFloatError(MyValueError):
   def __str__(self):
      return f"The given parameter {self.value} is a float and not an int."

class MyTypeError(MyValueError):
   def __init__(self, val, val_type):
       self.value_type = val_type
       super(MyTypeError, self).__init__(val)

   def __str__(self):
      return f"The given parameter {self.value} is of type {self.value_type} and not int."

class MyNegativeError(MyValueError):
   def __str__(self):
      return f"The given number {self.value} is not positive."

def positive(num):
   if type(num).__name__ == 'float':
       raise MyFloatError(num)

   if type(num).__name__ != 'int':
       raise MyTypeError(num, type(num).__name__)

   if num < 0:
       raise MyNegativeError(num)

for val in [14, 24.3, "hi", -10]:
   print(val)
   print(type(val).__name__)
   try:
      positive(val)
   except MyValueError as ex:
      print(f"Exception: {ex}")
      print(f"Exception type {type(ex).__name__}")

   # Exception, ValueError
