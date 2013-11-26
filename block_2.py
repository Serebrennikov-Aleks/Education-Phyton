Python 2.7.3 (default, Sep 26 2013, 20:08:41) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> def f(*args):
	"""
Написать функцию, которой можно передавать аргументы либо списком/кортежем, либопо одному. Функция производит суммирование всех аргументов.

>>> f(1, 2, 3)
6
>>> f([1, 2, 3])
6
>>> f((3, 5, 6))
14
>>> f(3, (5, 6))
14

        """
	result = 0
	for x in args:
		if not isinstance(x, list) and not isinstance(x, tuple):
			result += x
		elif isinstance(x, list):
			result += f(*x)
		else:
			b = list(x)
			result += f(*b)
	return result

>>> def addition(val):
	"""
Написать функцию-фабрику, которая будет возвращать функцию сложения с аргументом.
>>> add = addition(5)
>>> add(3)
8
>>> add(8)
13
>>> add = addition(10)
>>> add(5)
15
        """
	def add5(arg):
		return arg + val
	return add5

>>> def addition(val):
	"""
Написать функцию-фабрику, которая будет возвращать функцию сложения с аргументом.
>>> add = addition(5)
>>> add(3)
8
>>> add(8)
13
>>> add(10)
15
>>> add(-1)
4
>>> add([1, 2, 3])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    add([1, 2, 3])
  File "<pyshell#1>", line 3, in add5
    return arg + val
TypeError: can only concatenate list (not "int") to list
>>> add('q')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    add('q')
  File "<pyshell#1>", line 3, in add5
    return arg + val
TypeError: cannot concatenate 'str' and 'int' objects
>>> 
>>> add = addition(10)
>>> add(5)
15
        """
	def add5(arg):
		return arg + val
	return add5

>>> def addition_lambda(val):
	"""
Написать функцию-фабрику, которая будет возвращать функцию сложения с аргументом.
        """
		return (lambda arg:arg + val)
	
  File "<pyshell#6>", line 5
    return (lambda arg:arg + val)
   ^
IndentationError: unexpected indent
>>> def addition_lambda(val):
	return (lambda arg: arg + val)

>>> def addition_range(start, end):
	"""
Написать фабрику, аналогичную п.2, но возвращающей список таких функций

>>> additionals = addition_range(0, 5)
<function add5 at 0xa1601ec>
<function add5 at 0xb5f9db8c>
<function add5 at 0xb5f9db8c>
<function add5 at 0xb5f9db8c>
<function add5 at 0xb5f9db8c>
<function add5 at 0xb5f9db8c>
        """
	for i in range(start, end + 1):
		print addition(i)

		
>>> def mymap(func, args):
	"""
Написать аналог map:

первым аргументом идет либо функция, либо список функций
вторым аргументом — список аргументов, которые будут переданы функциям
полагается, что эти функции — функции одного аргумента

>>> add0 = addition(0)
>>> add1 = addition(1)
>>> add2 = addition(2)
>>> print mymap([add0, add1, add2], [1, 2, 3])
[(1, 2, 3), (2, 3, 4), (3, 4, 5)]
        """
	if isinstance(func, list):
		return [tuple(f(arg) for arg in args) for f in func]
	else:
		return [func(arg) for arg in args]

	
>>> 
