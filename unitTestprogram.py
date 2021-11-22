import unittest

def add(a,b):
    return a+b
class MyTestClass(unittest.TestCase):
    def test_one(self):
        self.assertEqual(add(6,5),11,"failed")
    def test_two(self):
        try:
            self.assertEqual(add(5,5),11,"not meeting pass criteria")
        except Exception as exe:
            print("failed due to "+ str(exe))


if __name__=='__main__':
    unittest.main