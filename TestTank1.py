import unittest
from Tank import Tank

class TestTank(unittest.TestCase):
	"""docstring for TestTank"""
	def testTankHasImage(self):
		tank = Tank()
		assert tank.image !=None, "There is no tank image"

if __name__ == '__main__':
	unittest.main()