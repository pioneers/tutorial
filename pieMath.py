#!/usr/bin/env python
import numpy as np

def add(*vals):
    vals_np = np.asarray(vals, dtype=np.float)
    return np.sum(vals_np)

def sub(*vals):
    return vals[0] - add(*vals[1:])

def mul(*vals):
	vals_np = np.asarray(vals, dtype=np.float)
	return np.prod(vals_np)

def div(*vals):
	return vals[0] * mul(*vals[1:])**-1
