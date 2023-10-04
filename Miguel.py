import unittest

def name():
    n = 'MIGUEL'
    return n

class Check(unittest.TestCase):
    def test(self):
        self.assertEqual(name(), 'MIGUEL')

if __name__=='__main__':
    unittest.main()