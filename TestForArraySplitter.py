from ArraySplitter import ArraySplitter
import unittest

class TestsForArraySplitter(unittest.TestCase):

    #Test an array of size 10 will be split into 2 groups of 5
    def test_10_divided_by_2_array(self):
        givenArray = [0,1,2,3,4,5,6,7,8,9]
        splitNumber = 2
        #For extra clarity, added print to see what we return in console
        print(str(ArraySplitter.splitArray(givenArray, splitNumber)))
        self.assertEqual(str(ArraySplitter.splitArray(givenArray,splitNumber)), "[[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]")

    #Test an array of size 6 will be split into 2 groups of 3
    def test_6_divided_by_2_array(self):
        givenArray = [0,1,2,3,4,5]
        splitNumber = 2
        #For extra clarity, added print to see what we return in console
        print(str(ArraySplitter.splitArray(givenArray, splitNumber)))
        self.assertEqual(str(ArraySplitter.splitArray(givenArray,splitNumber)), "[[0, 1, 2], [3, 4, 5]]")

    #Test an array of size 10 will be split into 3 groups with the remainder put into a 4th group
    def test_10_divided_by_3_array(self):
        givenArray = [0,1,2,3,4,5,6,7,8,9]
        splitNumber = 3
        #For extra clarity, added print to see what we return in console
        print(str(ArraySplitter.splitArray(givenArray, splitNumber)))
        self.assertEqual(str(ArraySplitter.splitArray(givenArray,splitNumber)), "[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]")

    #Test an array of size 5 will be split into 3 groups with the remainder put into a 4th group
    def test_5_divided_by_3_array(self):
        givenArray = [0,1,2,3,4]
        splitNumber = 3
        #For extra clarity, added print to see what we return in console
        print(str(ArraySplitter.splitArray(givenArray, splitNumber)))
        self.assertEqual(str(ArraySplitter.splitArray(givenArray,splitNumber)), "[[0], [1], [2], [3, 4]]")


if __name__ == '__main__':
    unittest.main()
