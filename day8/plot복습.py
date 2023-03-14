# import matplotlib.pyplot as plt

# plt.figure()
# x1=[0,1,2]
# y1=[0,1,2]
# x2=[0,1,2]
# y2=[0,1/2,1]
# x3=[0,1,2]
# y3=[0,2,4]
# plt.plot(x1,y1,x2,y2,x3,y3)
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("first order function")
# plt.show()



import matplotlib.pyplot as plt

plt.figure()
x1=[]
y1=[]
x2=[]
y2=[]
for i in range(-10,21):
    x1.append(i)
    y1.append(1*i+2)
    x2.append(i)
    y2.append(-3*i+1)
plt.plot(x1,y1,x2,y2)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("first order function")
plt.show()


