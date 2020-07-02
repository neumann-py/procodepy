import random
import numpy as np
import matplotlib.pyplot as plt

x = [random.gauss(3,1) for _ in range(4000)]
y = [random.gauss(4,2) for _ in range(4000)]
#print(x,y)
xx = []
yy = []
sig = []
for i in range(1,6):
    xx.append(i)
    r = random.uniform(2,3)
    rr = random.uniform(0,0.05)
    yy.append(random.gauss(np.sqrt(i),np.sqrt(i*0.05)))
    sig.append(np.sqrt(i*0.05))
print('xx=',xx)
print("yy=", yy)
print("sig=",sig)
x_array = np.array(x)
y_array =np.array(y)
z_array = (x_array/y_array)
#print(x_array,y_array,z_array)
plt.style.use('seaborn-deep')
bins = np.linspace(-10, 10, 250)
hist1 = plt.hist(z_array,bins, alpha = 1.0,color = 'blue',label ='ratio of two gaussian')
hist2 = plt.hist(x_array,bins, alpha = 0.5,color = 'red',label ='gaussian1')
hist3 = plt.hist(y_array,bins, alpha = 0.5,color = 'green',label ='gaussian2')
plt.legend(loc='upper right')
#plt.show()
'''pyplot.hist(x, bins, alpha=0.5, label='x')
pyplot.hist(y, bins, alpha=0.5, label='y')
pyplot.show()'''
