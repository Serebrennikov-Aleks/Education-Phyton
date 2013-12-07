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
		return function()
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

print func(1, 2)

# 3.Написать два декоратора:

# 3.1 принимает набор типов и проверяет, что входные параметры декарируемой функции соответствуют этим типам.
# аргументы декоратора!
def accepts(*pargs): 
	def my_decorator(func):
		# аргументы функции!
		def wrapped(*args) :
			for val in args:
				if not isinstance(val, pargs):
					errmsg = 'Argument %s not in %s' % (val, pargs)
					raise TypeError(errmsg)
			return func(*args)
		return wrapped 
	return my_decorator
 
@accepts(int, float)
def decorated_function_with_arguments(function_arg1, function_arg2):
	return ("Я - декорируемая функция и я знаю только о своих аргументах: {0}"
		   " {1}".format(function_arg1, function_arg2))
 
print decorated_function_with_arguments(2.12, 2.15)

# 3.2 принимает набор типов и проверяет, что результат работы функции соответствует этим типам.
# аргументы декоратора!
def returns(*pargs): 
	def my_decorator(func):
		# аргументы функции!
		def wrapped(*args) :
			out = func(*args)
			if not isinstance(out, pargs):
				errmsg = 'Argument %s not in %s' % (out, pargs)
				raise TypeError(errmsg)
			return out
		return wrapped 
	return my_decorator
 
@returns(int, float)
def decorated_function_with_arguments_returns(function_arg1, function_arg2):
	return function_arg1 + function_arg2
 
print decorated_function_with_arguments_returns(2, 2.15)
