numbers=[10,5,20,34,23,12,53,80]
largest= numbers[0]
for num in numbers:
  if num > largest:
    largest=num
print("largest number =",largest)