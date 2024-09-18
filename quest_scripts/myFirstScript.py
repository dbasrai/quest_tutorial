import numpy as np
from src.utils import *



num_workers = 10

my_data=[]
bias=10

for i in range(num_workers):
    my_data.append(np.random.rand(100,100,100))

def covary(matrix, bias):
    return matrix@matrix.T + bias

output = multipool(covary, bias, iterable=my_data, num_workers=num_workers)

pdump(output, '../picklejar/big_discovery.pickle')

print('success!')
