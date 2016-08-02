#!/usr/bin/env python
import duck

def test_add0():
	assert duck.add(1,2,3) == 6

def test_sub0():
	assert duck.sub(1,2,3) == -4

def test_sub1():
	assert duck.sub(1,2,'3') == -4

