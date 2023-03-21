import matplotlib.pyplot as plt

# plt.figure()
# x=[]
# y=[]
# x1=[]
# y1=[]
# for i in range(-10,11):
#     x.append(i)
#     y.append(i)
#     x1.append(i)
#     y1.append(i**2)
# plt.plot(x,y,x1,y1)
# plt.show()


# import matplotlib.pyplot as plt
# plt.figure()
# x=[]
# y=[]
# x1=[]
# y1=[]
# for i in range(-10,11):
#     x.append(i)
#     y.append(i**3)
#     x1.append(i)
#     y1.append(-i**3)
# plt.plot(x,y,x1,y1)
# plt.show()

# a = []
# for i in range(10):
#     a.append(i)
# print(a)

# b = []
# for i in range(2, 5):
#     b.append(i)
# print(b)

figure, axes = plt.subplots(2, 2)
fruits = ["apple", "banana", "blueberry", "orange"]
counts = [4, 6, 5, 10]
bar_color = ["red", "yellow", "blue", "orange"]
barh_color = ["black"]
barh_color1 = ["red"]

x1 = []
y1 = []
for i in range(-10, 11):
    x1.append(i)
    y1.append(i**2)

axes[0, 0].plot(x1, y1, "og")

axes[0, 1].barh(fruits, counts, color=barh_color1)
axes[1, 1].bar(fruits, counts, color=bar_color)
axes[1, 0].barh(fruits, counts, color=barh_color)
plt.show()
