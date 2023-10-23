def positive(num):
   if type(num).__name__ == 'float':
      raise Exception(f"The given parameter {num} is a float and not an int.")

   if type(num).__name__ != 'int':
      raise Exception(
          f"The given parameter {num} is of type {type(num).__name__} and not int."
      )

   if num < 0:
      raise Exception(f"The given number {num} is not positive.")

for val in [14, 24.3, "hi", -10]:
   print(val)
   print(type(val).__name__)
   try:
      positive(val)
   except Exception as ex:
      print(f"Exception: {ex}")
