#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  block_7.py
#  
#  Copyright 2014 alexander <shurik.18@mail.ru>
#  
#  

# 1.Для чего используются, какие аргументы получают, что должны возвращать: методы __new__ и __init__ классов
# __new__ - метод, который создает объект класса cls. Возвращает объект данного класса.
# __init__ - метод класса, который инициализирует созданный объект. Принимает в качестве параметров:
# self - экземпляр класса
# args - аргументы
# ничего не возвращает

# 2.Какие аргументы получает __new__ и __init__ у метакласса?
# __new__ - Параметры - name, bases, attrs. Возвращает класс.
# __init__ - с теми же параметрами и уже созданным классом.
#
#

# Задания

# 1.Реализовать дескрипторы, которые бы фиксировали тип атрибута
class Property(object):
	def __init__(self, value):
		self.__value = value
		self.__value_type = type(value)

	def __get__(self, obj, objtype):
		return self.__value

	def __set__(self, obj, value):
		if type(value) == self.__value_type:
			self.__value = value
		else:
			raise TypeError, "не могу установить атрибут"

class Image(object):
	height = Property(0)
	width = Property(0)
	path = Property('/tmp/')
	size = Property(0)

# 2.Реализовать базовый класс (используя метакласс), который бы фиксировал тип атрибута
class Image(object):
	height = Property(0)
	width = Property(0)
	path = Property('/tmp/')
	size = Property(0)


class ImageMetaclass(type):
	def __new__(cls, name, bases, attrs):
		for key, val in attrs.iteritems():
			if not key.startswith('_'):
				attrs[key] = Property(val)
		return type.__new__(cls, name, bases, attrs)

class ImageBase(object):
	__metaclass__ = ImageMetaclass
	height = 0
	width = 0
	path = '/tmp'
	size = 0

# 3.Реализовать базовый класс (используя метакласс) и дескрипторы, которые бы на основе класса создавали SQL-схему (ANSI SQL) для модели:
class Integer(object):
	def __get__(self, obj, objtype):
		return 'integer'

class Str(object):
	def __init__(self,limit):
		self.limit = limit
	def __get__(self, obj, objtype):
		return 'varchar(%d)' % self.limit

class TableMetaclassSQL(type):
	def __new__(cls, name, bases, attrs):
		def sql():
			stringResult = 'CREATE TABLE %s (' % name.lower() + '\n '
			listAttrs = []
			for key, val in attrs.iteritems():
				if isinstance(attrs[key], Integer):
					listAttrs.append(key + ' integer')
				elif isinstance(attrs[key], Str):
					listAttrs.append(key + ' varchar(%s)' % attrs[key].limit)
			stringResult += ',\n '.join(listAttrs) + ',\n)'
			return stringResult
		attrs['sql'] = sql()
		return type.__new__(cls, name, bases, attrs)

class Table(object):
	__metaclass__ = TableMetaclassSQL

class ImageStep3(Table):
	height = Integer()
	width = Integer()
	path = Str(128)

if __name__ == '__main__':
	img = Image()
	img.height = 340
	print img.height
	img.path = '/tmp/x00.jpeg'
	print img.path
	img.path = 'test'
	print img.path
	#img.size = 'test'
	print ImageStep3.sql
