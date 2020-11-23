import unittest
import test

class TestCase(unittest.TestCase):
    def setUp(self):
            self.args = {
                              'hired': {
                                'be': {
                                  'to': {
                                    'deserve': 'I'
                                  }
                                }
                              }
                            }

    def tearDown(self):
        self.args = None

    def test_reverseDict_Dict(self):
        expected = {
                          'I': {
                            'deserve': {
                              'to': {
                                 'be': 'hired'
                              }
                            }
                          }
                        }
        result = test.reverseDict(self.args);
        self.assertEqual(expected, result);

    def test_reverseDict_NullDict(self):
        expected = {}
        result = test.reverseDict({});
        self.assertEqual(expected, result);

    def test_reverseDict_NotDict(self):
        expected = 'e'
        result = test.reverseDict('e');
        self.assertEqual(expected, result);
        
suite = unittest.TestSuite()
suite.addTest(TestCase('test_reverseDict_Dict'))
suite.addTest(TestCase('test_reverseDict_NullDict'))
suite.addTest(TestCase('test_reverseDict_NotDict'))
unittest.TextTestRunner(verbosity=2).run(suite)