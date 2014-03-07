import unittest
from lakitu import Lakitu

class TestLakitu(unittest.TestCase):
	def test_display_instances(self):
		user = "testUser"
		password = "testPassword"
		lakitu = Lakitu(user,password)
		result = lakitu.display_instances()
		self.assertEqual("{0}:{1}".format(user, password), result)

if __name__ == "__main__":
    unittest.main()