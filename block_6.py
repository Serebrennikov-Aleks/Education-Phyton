#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  block_6.py
#  
#  Copyright 2013 alexander <shurik.18@mail.ru>
#  
#  
#  

#1. Написать базовый класс Observable, который бы позволял наследникам:
#a. при передаче **kwargs заносить соответствующие значения как атрибуты
#b. сделать так, чтобы при print отображались все публичные атрибуты

class Observable:
	def __init__(self, **kwargs):
		for key, value in kwargs.iteritems():
			self.__dict__[key] = value
	def gatherAttrs(self):
		attrs = []
		for key in self.__dict__:
			if not key.startswith('_') and not key.startswith('__'):
				attrs.append('%s=%s' % (key, getattr(self, key)))
		return ', '.join(attrs)
	def __str__(self):
		return '%s(%s)' % (self.__class__.__name__, self.gatherAttrs())


class X(Observable):
	pass

#2. Написать класс, который бы по всем внешним признакам был бы словарем, но позволял обращаться к ключам как к атрибутам.

class DictAttr:
	def __init__(self, *args):
		self.dicts = {}
		for key in args:
			self.dicts = dict(key)
			for x, y in key:
				self.__dict__[x] = y

	def __getitem__(self, key):
		return self.dicts[key]

	def __getattr__(self, attr):
		"""
		Вызывается при обращении к отсутствующему атрибуту
		"""
		raise AttributeError(attr)

	def get(self, *args):
		if len(args) == 2:
			return args[1]
		elif len(args) == 1:
			if args[0] in self.__dict__:
				return getattr(self, args[0])
			else:
				raise AttributeError(args)

	def __str__(self):
		return '%s' % self.dicts

#3.Пункт 2 с усложнением: написать родительский класс XDictAttr так, чтобы у наследника динамически определялся ключ по наличию метода get_<KEY>.

class XDictAttr(object):
	def __init__(self, *args):
		self.dicts = {}
		for key in args:
			self.dicts = dict(key)
			for x, y in key:
				self.__dict__[x] = y

	def __getattr__(self, attr):
		"""
		Вызывается при обращении к отсутствующему атрибуту
		"""
		res = self.gatherAttrs(attr)
		if res:
			return res
		raise AttributeError(attr)

	def __getitem__(self, key):
		res = self.gatherAttrs(key)
		if res:
			return res
		return self.dicts[key]

	def get(self, *args):
		res = self.gatherAttrs(args[0])
		if res:
			return res
		elif len(args) == 2:
			return args[1]
		elif len(args) == 1:
			if args[0] in self.__dict__:
				return getattr(self, args[0])
			else:
				raise AttributeError(args)

	def gatherAttrs(self, name):
		attr = 'get_' + name
		if attr in self.__class__.__dict__:
			fn = object.__getattribute__(self,'get_' + name)
			val = fn()
			return val
		return 0


	def __str__(self):
		return '%s' % self.dicts

class Xstep3(XDictAttr):
	def get_foo(self):
		return 5
	def get_bar(self):
		return 12
	def get_bzz(self):
		return 'missing'

#4. Написать класс, который регистрирует свои экземпляры и предоставляет интерфейс итератора по ним
class Interface(type):
	def __iter__(cls):
		return iter(cls._example)
		#return cls._example.__iter__()

class Reg:
	
	_example = []
	__metaclass__ = Interface

	def __init__(self):
		self._example.append(self)

if __name__ == '__main__':
	#1
	x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
	print x.foo
	print x.bar
	print x._bazz
	print x.name
	print x.props
	print x
	#2
	x = DictAttr([('one', 1), ('two', 2), ('three', 3)])
	print x['one']
	print x['two']
	print x['three']
	print x.one
	print x.two
	print x.three
	#print x.five
	print x.get('one')
	print x.get('two')
	print x.get('three')
	#print x.get('five')
	print x.get('five', 'missing')
	#3
	x = Xstep3([('one', 1), ('two', 2), ('three', 3)])
	print x['one']
	print x['two']
	print x['three']
	print x.one
	print x.two
	print x.three
	#print x.five
	print x.get('one')
	print x.get('two')
	print x.get('three')
	#print x.get('five')
	print x.get('five', 'missing')
	print x.bar
	print x['foo']
	print x.get('foo', 'missing')
	print x.get('bzz', 'missing')
	#4
	x = Reg()
	print x
	y = Reg()
	print y
	z = Reg()
	print z
	#print type(Test.__iter__)
	for i in Reg:
		print i
