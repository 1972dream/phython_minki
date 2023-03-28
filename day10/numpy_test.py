import numpy as np

c = np.array([1, 2, 3, 4, 5])
print(c)
a = [1, 2, 3, 4, 5]
print(a)
b = [6, 7, 8, 9, 10]
print(a + b)
d = np.array([6, 7, 8, 9, 10])
print(c / d)
"""
slicing
전체중 일부만 선택하는 방법
<하나만 가르키는 것은 indexing>
문법
리스트[시작:끝]
      이상:미만
*":" = "~"
"""
fruits = ["apple", "banana", "orange", "watermelon"]
# fruits.clear()
# fruits.append("apple")
# fruits.append("banana")
# print(fruits)
# print(fruits[:])
y = []

for i in range(20, 30, 2):
    if i % 3 != 0:
        y.append(i)
print(y[:4])
