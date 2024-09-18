#genutils
import pickle
import numpy as np
from concurrent.futures import *

def pload(pickle_path):
    with open(pickle_path, 'rb') as f:
        return pickle.load(f)

def pdump(object, pickle_path):
    with open(pickle_path, 'wb') as f:
        pickle.dump(object, f)

def multipool(function, *args, iterable, num_workers):
    #function runs on each element in iterable
    #first argument in function is the element

    result = [None] * len(iterable)
    executor = ProcessPoolExecutor(max_workers = num_workers)

    for idx, i in enumerate(iterable):
        result[idx] = executor.submit(function, i, *args)

    wait(result, timeout=None, return_when=ALL_COMPLETED)

    output = []
    for this_result in result:
        output.append(this_result.result())

    return output
