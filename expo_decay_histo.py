#program to generate 1000 uniform random no.
#calculate the sample mean
# repeat this 10K times
#Plot it in a histogram, check rms of that using formula of urself
# Repeat all of the above process but now with 100 random nos.
'''         Amann Gupta (PMSc-- *********SAHA INSTITUTE OF NUCLEAR PHYSICS*********)
            **********************January 23, 2020**********************************'''
import random
import numpy as np
from numpy import mean, sqrt, arange, square
import matplotlib.pyplot as plt
sample_mean1k = []
rms1k = []
#sample_mean1k_sqr =[]
for i in range(1):
    sample_mean1k_sqr =[]
    rnd_uniform  = [np.random.uniform(0,1) for _ in range(10)]
    #print(rnd_uniform, len(rnd_uniform))
    sample_mean1k.append(sum(rnd_uniform)/len(rnd_uniform))
#print(sample_mean1k)
    sample_mean1k_array = np.array(sample_mean1k)
    rnd_uniform_array = np.array(rnd_uniform)
    sample_data_sqr = rnd_uniform_array*rnd_uniform_array
    sample_data_sqr_mean = (sum(sample_data_sqr)/len(sample_data_sqr))
    rms1k.append(sqrt(sample_data_sqr_mean))
print(rms1k)
#rms_mean1 = np.sqrt(np.mean(sample_mean1k_array**2))
#rms_mean1 = np.sqrt(np.mean(sample_mean1k_array**2))
#print('signa_mean =',np.std(sample_mean1k_array))
#print('sigma =',np.std(rnd_uniform_array))
#rms1k_array = np.array(rms1k)
#print(np.std(rms1k_array))
#print(rms_mean1)
#=========================================ANOTHER EXPERIMENT OF 100 RANDOM NOS.============================
'''sample_mean100 = []
rms100 =[]
for i in range(1000):
    sample_mean100_sqr =[]
    rnd_uniform  = [random.uniform(0,1) for _ in range(100)]
    #expornd = (-1)*log(1-rnd_uniform)
    #print(rnd_uniform, len(rnd_uniform))
    sample_mean100.append(sum(rnd_uniform)/len(rnd_uniform))
#print(sample_mean100)
    sample_mean100_array = np.array(sample_mean100)
    rnd_uniform_array = np.array(rnd_uniform)
    sample_mean100_sqr = rnd_uniform_array*rnd_uniform_array
    sample_mean100_sqr_mean = (sum(sample_mean100_sqr)/len(sample_mean100_sqr))
    rms100.append(sqrt(sample_mean100_sqr_mean))
#print(rms100)
#rms100_array = np.array(rms100)
#print(np.std(rms100_array))
#rms_mean100 = np.sqrt(np.mean(sample_mean100_array**2))
#print(rms_mean100)
print('signa_mean =',np.std(sample_mean100_array))
print('sigma =',np.std(rnd_uniform_array))
#=========================================ANOTHER EXPERIMENT OF 10 RANDOM NOS.============================

sample_mean10 = []
rms10 =[]
for i in range(1000):
    sample_mean10_sqr =[]
    rnd_uniform  = [random.uniform(0,1) for _ in range(10)]
    #expornd = (-1)*log(1-rnd_uniform)
    #print(rnd_uniform, len(rnd_uniform))
    sample_mean10.append(sum(rnd_uniform)/len(rnd_uniform))
#print(sample_mean100)
    sample_mean10_array = np.array(sample_mean10)
    rnd_uniform_array = np.array(rnd_uniform)
    sample_mean10_sqr = rnd_uniform_array*rnd_uniform_array
    sample_mean10_sqr_mean = (sum(sample_mean10_sqr)/len(sample_mean10_sqr))
    rms10.append(sqrt(sample_mean10_sqr_mean))
#print(rms100)
#rms10_array = np.array(rms10)
#print(np.std(rms10_array))
#rms_mean10 = np.sqrt(np.mean(sample_mean10_array**2))
#print(rms_mean10)
print('signa_mean =',np.std(sample_mean10_array))
print('sigma =',np.std(rnd_uniform_array))'''
#==============================Plotting========================================
'''plt.style.use('seaborn-deep')
bins = np.linspace(0.4,0.6,100)
bins2 = np.linspace(0.5,0.7,100)
fig, ((ax0, ax1),(ax2, ax3)) = plt.subplots(nrows=2, ncols=2)
colors = ['red', 'tan', 'lime']
hist1 = ax0.hist(sample_mean1k, bins, color = 'red', label = 'Sample mean of 1000 random #s')
#hist1 = ax0.hist(rms10, bins2, color = 'red', label = 'RMS for 10 random #s')
ax0.legend(prop={'size': 7})
hist2 = ax1.hist(sample_mean100, bins, color = 'blue', label = 'Sample mean of 100 random #s')
ax1.legend(prop={'size': 7})
hist3 = ax2.hist(sample_mean10, bins, color = 'green', label = 'Sample mean of 10 random #s')

#hist3 = ax2.hist(rms1k, bins2, label = 'RMS for 1000 random #s')
ax2.legend(prop={'size': 7})
hist4 = ax3.hist(rms100, bins2, label = 'RMS for 100 random #s')
ax3.legend(prop={'size': 7})


#hist2 = plt.hist((data2), bins = 100)
#plt.legend(loc='upper right')
plt.show()'''



'''plt.style.use('seaborn-deep')
bins = np.linspace(0.4,0.6,1000)
hist1 = plt.hist(sample_mean1k, bins, color = 'red', label = 'Sample mean of 1000 random #s')
hist2 = plt.hist(sample_mean100, bins, color = 'blue', label = 'Sample mean of 100 random #s')
plt.legend(loc='upper right')
plt.show()'''
