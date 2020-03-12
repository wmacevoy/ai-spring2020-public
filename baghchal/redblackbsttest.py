import unittest

from redblackbst import RedBlackBST

class RedBlackBSTTest(unittest.TestCase):
    def testDefault(self):
        t : RedBlackBST[int,str] = RedBlackBST[int,str]()
        testKey : int = 1
        testValue : str = "one"

        self.assertEqual(t.size,0)
        self.assertEqual(t.empty,True)
        self.assertEqual(t.contains(testKey),False)

        t.put(testKey,testValue)
        self.assertEqual(t.size,1)
        self.assertEqual(t.empty,False)
        self.assertEqual(t.contains(testKey),True)

        t.delete(testKey)

        self.assertEqual(t.size,0)
        self.assertEqual(t.empty,True)
        self.assertEqual(t.contains(testKey),False)

if __name__ == '__main__':
    unittest.main()
