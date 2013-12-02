#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  block_2.py
#  
#  Copyright 2013 alexander <shurik.18@mail.ru>
#
# 1.Написать функцию, которой можно передавать аргументы либо списком/кортежем, либо по одному. Функция производит суммирование всех аргументов.
def f(*args):
	"""
	>>> f(1)
	1
	>>> f(2, 2)
	4
	>>> f(1, 2, (3, 4))
	10
	>>> f(10, ())
	10
	"""
	result = 0
	for x in args:
		if isinstance(x, list):
			result += f(*x)
		elif isinstance(x, tuple):
			result += f(*(list(x)))
		else:
			result += x
	return result
	
# 2.Написать функцию-фабрику, которая будет возвращать функцию сложения с аргументом.
def addition(val):
	"""
	>>> add = addition(5)
	>>> add(3)
	8
	>>> add = addition(-1)
	>>> add(3)
	2
	>>> add = addition('s')
	>>> add(3)
	Traceback (most recent call last):
	...
	TypeError: unsupported operand type(s) for +: 'int' and 'str'
	"""
	def add5(arg):
		return arg + val
	return add5

# 2.2 Используя lambda-функцию
def addition_lambda(val):
	"""
	>>> add = addition_lambda(5)
	>>> add(3)
	8
	>>> add = addition_lambda(-1)
	>>> add(3)
	2
	>>> add = addition_lambda('s')
	>>> add(3)
	Traceback (most recent call last):
	...
	TypeError: unsupported operand type(s) for +: 'int' and 'str'
	"""
	return (lambda arg: arg + val)

# 3.Написать фабрику, аналогичную п.2, но возвращающей список таких функций
def addition_range(start, end):
	"""
	>>> print addition_range(0, 3)
	[<function add5 at 0xb7285b1c>, <function add5 at 0xb7285b54>, <function add5 at 0xb6ea2bc4>, <function add5 at 0xb6ea2bfc>]
	"""
	return [addition(i) for i in range(start, end + 1)]

# 4.Написать аналог map
def mymap(func, args):
	"""
	>>> add0 = addition(0)
	>>> add1 = addition(1)
	>>> add2 = addition(2)
	>>> print mymap([add0, add1, add2], [1, 2, 3])
	[(1, 2, 3), (2, 3, 4), (3, 4, 5)]
	>>> print mymap([], [])
	[]
	>>> print mymap(sum, [(3, 4, 5, 6, 2, 6)])
	[26]
	"""
	if isinstance(func, list):
		return [tuple(f(arg) for arg in args) for f in func]
	else:
		return [func(arg) for arg in args]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
