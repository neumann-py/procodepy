import matplotlib.pyplot as plt
import scipy.stats as st
#import pandas as pd
import numpy as np
import numpy.random as npr
import bootstrapped.bootstrap as bs
import bootstrapped.compare_functions as bs_compare
import bootstrapped.stats_functions as bs_stats
import collections
mean = 100
stdev = 10

population = np.random.normal(loc=mean, scale=stdev, size=50000)
samples = population[:1000]
# Plot the population
#count, bins, ignored = plt.hist(population, 30, normed=True)
print(np.std([samples], axis =1))
#plt.title('Distribution of the population')
#plt.show()
# calculate bootstrap estimates for the mean and standard deviation
mean_results = bs.bootstrap(samples, stat_func=bs_stats.mean)

# see advanced_bootstrap_features.ipynb for a discussion of how to use the stat_func arg
stdev_results = bs.bootstrap(samples, stat_func=bs_stats.std)
print('Bootstrapped mean should be: {}'.format(mean))
print('\t' + str(mean_results))
print('')
print('Bootstrapped stdev should be: {}'.format(stdev))
print('\t' + str(stdev_results))
