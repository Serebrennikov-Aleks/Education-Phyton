#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  block_4_iterator.py
#  
#  Copyright 2013 alexander <shurik.18@mail.ru>
#  
#  

class cycle():
	def __init__(self, data):
		self.data = [i for i in data]
		self.index = -1
		self.end = len(self.data)
	def __iter__(self):
		return self
	def next(self):
		if self.index == (self.end - 1):
			self.index = 0
		else:
			self.index += 1
		return self.data[self.index]

class chain():
	def __init__(self, *data):
		self.data = [obj for iterator in data for obj in iterator]
		self.index = -1
		self.end = len(self.data)
	def __iter__(self):
		return self
	def next(self):
		if self.index == (self.end - 1):
			raise StopIteration
		else:
			self.index += 1
		return self.data[self.index]

print "cycle"

i = iter([1, 2, 3])
it = cycle(i)
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()

print "chain"

i1 = iter([1, 2, 3])
i2 = iter([4, 5])
i3 = iter([6, 7, 8])
it = chain(i1, i2, i3)
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
