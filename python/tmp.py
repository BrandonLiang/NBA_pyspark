#!/bin/python
from itertools import permutations

l = [1,3,4,6]

output = []
for element in list(permutations(l)):
  output_1 = []
  first = element[0]
  second = element[1]
  output_1.append(first + second)
  output_1.append(first - second)
  output_1.append(second - first)
  output_1.append(first * second)
  output_1.append(first * 1.0 / second)
  output_1.append(second * 1.0 / first)
  output.append(output_1)

print(output)
