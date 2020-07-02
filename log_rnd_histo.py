#program to plot the histogram of logarithmic random no. distribution
import numpy as np
import matplotlib.pyplot as plt
import random
rnd_uniform = [random.uniform(0,9) for _ in range(10000)]
rnd_log = -np.log(rnd_uniform)
#print(rnd_uniform)
plt.style.use('seaborn-deep')
bins = np.linspace(0,9,500)
#hist1 = plt.hist(rnd_uniform, bins, color = 'red', label = 'Uniform random no.')
hist2 = plt.hist(rnd_log, bins, color = 'blue', label = 'logarithmic random no.')
plt.legend(loc='upper right')
plt.show()
