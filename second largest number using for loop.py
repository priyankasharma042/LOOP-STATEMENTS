numbers=[0,25,50,34,23,20]
first=numbers[0]
second=numbers[0]
for i in numbers:
  if i>first:
      second=first
      first=i
  elif i>second and i !=first:
      second=i
print("second",second)
