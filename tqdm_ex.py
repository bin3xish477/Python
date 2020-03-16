#!/usr/bin/env python3

from tqdm import tqdm

multiply_itself = lambda x : x * x

for i in tqdm(range(100000000), desc='Progress'):
	multiply_itself(i)
