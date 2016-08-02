#!/usr/bin/env python
import pieMath

def test_add0():
    assert pieMath.add(1,2,3) == 6

def test_sub0():
    assert pieMath.sub(1,2,3) == -4

def test_sub1():
    assert pieMath.sub(1,2,'3') == -4

def test_mul0():
    assert pieMath.mul(1,2,3) == 6

def test_div0():
    assert pieMath.div(3,2,1) == 1.5
