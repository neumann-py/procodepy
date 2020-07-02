import matplotlib.pyplot as plt
import random
import numpy as np
#import math, Latex
#import seaborn as sns
#settings for seaborn plotting
#sns.set(color_codes = True)
#setting for seaborn plot size
#sns.set(rc={'figure.figsize':(5,5)})

poiss = []
data =  np.random.poisson(5,10000)   #poisson(k,lambda); lambda is parameter
poiss.append(data)
plt.style.use('seaborn-deep')
#bins = np.linspace(0,9,500)
hist2 = plt.hist(poiss, bins = 100, color = 'blue',density = False, label = 'poisson distribution')
plt.title('Histogram of poisson distribution')
plt.legend(loc='upper right')
plt.show()
