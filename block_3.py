#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  block_3.py
#  
#  Copyright 2013 alexander <shurik.18@mail.ru>
#  
#  
# Декоратор - это функция, ожидающая ДРУГУЮ функцию в качестве параметра

# 1.Написать декоратор добовляющий к докстрингам функции фразу "I'm was here!:)".

def my_decorator(function):
	def the_original_function():
		print function()
	the_original_function.__doc__ = "I'm was here!:)"
	return the_original_function

@my_decorator
def func():
	return 42
 
#func()
#help(func)

# 2.Написать декоратор который cчитает время выполнения функции.

import time
def timer(function):
	def tmp(x, y):
		t = time.time()
		res = function(x, y)
		print "Время выполнения функции: %f" % (time.time()-t)
		return res

	return tmp

@timer
def func(x, y):
	return x + y

#print func(1, 2)

# 3.Написать два декоратора - впроцессе....
