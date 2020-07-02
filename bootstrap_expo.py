import numpy as np
import math
import random
import matplotlib.pyplot as plt
import bootstrapped.bootstrap as bs
import bootstrapped.stats_functions as bs_stats

def gen(a):
    y = np.random.randint(1,10)
    return(-np.log(y)*(a))
#pdf = (1/a)* exp(-x/a) with a = 1 = mean of pdf
N = 10
rnd = np.zeros(N)
rnd_list = []
for i in range(N):
    rnd[i] = gen(1.0)           #np.random.randint(1,10)
print('sample mean without bootstrapping =', np.mean(rnd))
print('sigma of sample without bootstrapping =', np.std(rnd))
number_of_samples = len(rnd)
NN =10000        # actaully it should be N**N
sample_mean_bs = np.zeros(NN)
random_items =[random.choices(population=rnd, k=number_of_samples) for x in range(NN)]
random_items_array = np.array(random_items)
#print(random_items_array)
#print(sum(random_items_array[0]))
list_of_sample_mean_bs = []
for i in range(NN):
    sample_mean_bs[i] = np.mean(random_items_array[i])
    #print(np.mean(random_items_array[i]), random_items_array[i], i)
    #print(sample_mean_bs[i],i)
    list_of_sample_mean_bs.append(sample_mean_bs[i])
#print('list_of_sample_mean_bs', list_of_sample_mean_bs)
print('mean_sample_mean_bs', np.mean(list_of_sample_mean_bs))
print('sigma of_sample_mean_bs', np.std(list_of_sample_mean_bs))
#print(np.std(rnd))
#suum_mean = sum(random_items_array)/NN
#print('summ mean =', suum_mean)
#print('sample mean after bootstrapping = ',np.mean(random_items_array))
plt.style.use('seaborn-deep')
#bins = np.linspace(0,9,500)
#hist1 = plt.hist(rnd_uniform, bins, color = 'red', label = 'Uniform random no.')
hist2 = plt.hist(sample_mean_bs, bins = 400, color = 'blue', label = 'sample_mean_bs')
plt.title('Histogram of sample means using boostrap method')
plt.legend(loc='upper right')
plt.show()


#===============================================================================
#population = np.random.normal(loc=mean, scale=stdev, size=50)
''''population = [gen(1.0) for x in range(50)]
# take 1k 'samples' from the larger population
sample = population[:10]
samples = np.array(sample)
#print(population)
print(samples)
print(bs.bootstrap(samples, stat_func=bs_stats.mean))
print(bs.bootstrap(samples, stat_func=bs_stats.std))'''
