#program to plot a histograms for random numbers
# and to check that the hostogram of  sum of two random numbers
#results in a triangular shape histogram
import numpy
import random
import matplotlib.pyplot as plt
data12 = []
data123 = []
data1 = [random.randint(0, 9) for _ in range(10000)]
data2 = [random.randint(0, 9) for _ in range(10000)]
data3 = [random.randint(0, 9) for _ in range(10000)]
data4 = [random.randint(0, 9) for _ in range(10000)]
data5 = [random.randint(0, 9) for _ in range(10000)]

data12 = [sum(x) for x in zip(data1,data2)]
data123 = [sum(x) for x in zip(data1,data2,data3,data4,data5)]

#print(data1)
#print( data2)
#print( data)
#data2 = [random.randint(0, 1) for _ in range(1000)]
#print(data)
plt.style.use('seaborn-deep')
bins = numpy.linspace(0,18,100)
bins2 = numpy.linspace(0,45,100)
fig, ((ax0, ax1),(ax2, ax3)) = plt.subplots(nrows=2, ncols=2)
colors = ['red', 'tan', 'lime']
hist1 = ax0.hist(data1, bins, color = 'red', label = 'data1')
ax0.legend(prop={'size': 7})
hist2 = ax1.hist(data2, bins, color = 'green', label = 'data2')
ax1.legend(prop={'size': 7})
hist3 = ax2.hist(data12, bins, label = 'Convolution (data1 + data2)')
ax2.legend(prop={'size': 7})
hist4 = ax3.hist(data123, bins2, label = 'Convolution (data1 + data2+data3)')
ax3.legend(prop={'size': 7})

#hist2 = plt.hist((data2), bins = 100)
#plt.legend(loc='upper right')
plt.show()
