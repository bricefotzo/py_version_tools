import unittest
from version_tools.version_tools.version import *


class TestVersion(unittest.TestCase):
    def test_get_current_version(self):
        self.assertEqual(get_current_version('.'),'0.1.2')
    def test_get_previous_version(self):
        self.assertEqual(get_previous_version('.'),'0.1.1')

    def test_inc_version(self):
        self.assertEqual(increment_version('0.0.1','patch'),'0.0.2')
        self.assertEqual(increment_version('0.0.3','minor'),'0.1.3')
        self.assertEqual(increment_version('0.5.21','major'),'1.5.21')

if __name__ == '__main__':
    unittest.main()