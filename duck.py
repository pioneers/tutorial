#! /usr/bin/env python
import numpy as np

def add(*coeffs):
    coeffs_np = np.asarray(coeffs, dtype=np.float)
    return np.dot(coeffs_np, np.ones(len(coeffs))).tolist()

def sub(*coeffs):
    return coeffs[0] - add(*coeffs[1:])
