import unittest
from block_6 import *

class TestX(unittest.TestCase):
	def setUp(self):
		self.x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))

	def test_(self):
		pass

	def test_foo_returns_1_for_foo_after_creation_with_X(self):
		self.assertEqual(1, self.x.foo)

	def test_name_returns_Amok_for_name_after_creation_with_X(self):
		self.assertEqual('Amok', self.x.name)

	def test_bazz_returns_12_for_bazz_after_creation_with_X(self):
		self.assertEqual(12, self.x._bazz)

	def tearDown(self):
		del self.x

class TestDictAttr(unittest.TestCase):
	def setUp(self):
		self.x = DictAttr([('one', 1), ('two', 2), ('three', 3)])

	def test_(self):
		pass

	def test_three_returns_3_for_three_after_creation_with_DictAttr(self):
		self.assertEqual(3, self.x['three'])

	def test_get_One_returns_Amok_for_get_One_after_creation_with_DictAttr(self):
		self.assertEqual(1, self.x.get('one'))

	def test_get_returns_missing_for_get_after_creation_with_DictAttr(self):
		self.assertEqual('missing', self.x.get('five', 'missing'))

	def test_one_returns_Amok_for_one_after_creation_with_DictAttr(self):
		self.assertEqual(1, self.x.one)

	def tearDown(self):
		del self.x

class TestXstep3(unittest.TestCase):
	def setUp(self):
		self.x = Xstep3([('one', 1), ('two', 2), ('three', 3)])

	def test_(self):
		pass

	def test_three_returns_3_for_three_after_creation_with_Xstep3(self):
		self.assertEqual(3, self.x['three'])

	def test_get_One_returns_Amok_for_get_One_after_creation_with_Xstep3(self):
		self.assertEqual(1, self.x.get('one'))

	def test_get_returns_missing_for_get_after_creation_with_Xstep3(self):
		self.assertEqual('missing', self.x.get('five', 'missing'))

	def test_one_returns_Amok_for_one_after_creation_with_Xstep3(self):
		self.assertEqual(1, self.x.one)

	def test_bar_returns_12_for_bar_creation_with_Xstep3(self):
		self.assertEqual(12, self.x.bar)

	def test_foo_returns_12_for_foo_creation_with_Xstep3(self):
		self.assertEqual(5, self.x['foo'])

	def test_foo_returns_missing_for_foo_creation_with_Xstep3(self):
		self.assertEqual(5, self.x.get('foo', 'missing'))

	def test_bzz_returns_missing_for_bzz_creation_with_Xstep3(self):
		self.assertEqual('missing', self.x.get('bzz', 'missing'))

	def tearDown(self):
		del self.x

if __name__ == '__main__':
	unittest.main()
