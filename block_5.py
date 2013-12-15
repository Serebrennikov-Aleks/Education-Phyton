#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Без block_5.py
#  
#  Copyright 2013 alexander <shurik.18@mail.ru>
#  
#  
#  

# 1.У нас есть импортированный модуль foo, как узнать физический путь файла, откуда он импортирован?
foo.__file__

# 2.Из модуля foo вы импортируете модуль feedparser.
# Версия X feedparser'а есть в общесистемном каталоге site-packages, версия Y — рядом с модулем foo.
# Определена переменная окружения PYTHONPATH, и там тоже есть feedparser, версии Z.
# Какая версия будет использоваться?

# Поиск модуля осуществляется из следующих источников:
# 1.	 Домашний каталог программы.
# 2.	 Содержимое переменной окружения PYTHONPATH (если таковая определена).
# 3.	 Каталоги стандартной библиотеки.
# 4.	 Содержимое любых файлов с расширением .pht (если таковые имеются).

# Ответ - будет использована Y версия.

# 3.Как посмотреть список каталогов, в которых Python ищет модули?
import sys
print sys.path

# 4. У вас есть модуль foo, внутри него импортируется модуль bar. Рядом с модулем foo есть файлы bar.py и bar/__init__.py Какой модуль будет использоваться.
# Ответ - будет загружен bar/__init__.py, в этом случае используется пакет.

# 5.Что означает и для чего используется конструкция __name__ == '__main__'
# Ответ - 
# Благодаря этому модуль может определить, был ли он запущен как самостоятельная программа 
# или импортирован другим модулем.
# - Если файл запускается как главный файл программы, атрибуту __name__ на
# запуске присваивается значение “__main__”.
# - Если файл импортируется, атрибуту __name__ присваивается имя модуля,
# под которым он будет известен клиенту.


def main():	
	return 0

if __name__ == '__main__':
	main()