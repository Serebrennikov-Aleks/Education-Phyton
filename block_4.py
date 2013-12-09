#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  block_4.py
#  
#  Copyright 2013 alexander <shurik.18@mail.ru>
#  
#  

# 1.Написать функцию-генератор cycle которая бы возвращала циклический итератор.
def cycle(iterl):
	"""
	>>> i = iter([1, 2, 3])
	>>> c = cycle(i)
	>>> c.next()
	1
	>>> c.next()
	2
	>>> c.next()
	3
	>>> c.next()
	1
	>>> c.next()
	2
	>>> 
	"""
	list_iterator = [i for i in iterl]
	k = len(list_iterator)
	i = 0
	while 1:
		if i < k:
			yield list_iterator[i]
			i += 1
		else:
			i = 0

# 2.Написать функцию-генератор chain, которая последовательно итерирует переданные объекты (произвольное количество)

def my_chain(*karg):
	"""
	>>> i1 = iter([1, 2, 3])
	>>> i2 = iter([4, 5])
	>>> i3 = iter([6, 7, 8])
	>>> c = my_chain(i1, i2, i3)
	>>> c.next()
	1
	>>> c.next()
	2
	>>> c.next()
	3
	>>> c.next()
	4
	>>> c.next()
	5
	>>> c.next()
	6
	>>> c.next()
	7
	>>> c.next()
	8
	>>> c.next()
	Traceback (most recent call last):
	  File "<pyshell#23>", line 1, in <module>
		c.next()
	StopIteration
	>>> 
	"""
	for iterator in karg:
		for obj in iterator:
			yield obj

i1 = iter([1, 2, 3])
i2 = iter([4, 5])
i3 = iter([6, 7, 8])
c = my_chain(i1, i2, i3)

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
