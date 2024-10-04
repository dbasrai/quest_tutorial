import numpy as np
from src.utils import *



num_workers =10

my_data=[]
bias=10

for i in range(50):
    my_data.append(np.random.rand(5000,100))

def covinv(matrix, bias):
    cov = matrix.T@matrix
    return np.linalg.inv(cov)+bias

output = multipool(covinv, bias, iterable=my_data, num_workers=num_workers)

pdump(output, '../picklejar/big_discovery.pickle')

print('success!')
