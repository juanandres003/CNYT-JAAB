import libcomplex as lc
import unittest
import math

class TestComplexOperations(unittest.TestCase):

    def test_complexsum(self):
        self.assertAlmostEqual(lc.cplxsum((1,2),(3,4)), (4,6))
        self.assertAlmostEqual(lc.cplxsum((5,6),(2,3)), (7,9))
    
    def test_complexprod(self):
        self.assertAlmostEqual(lc.cplxprod((1,2),(3,4)), (-5,10))
        self.assertAlmostEqual(lc.cplxprod((5,6),(2,3)), (-8,27))

    def test_complexrest(self):
        self.assertAlmostEqual(lc.cplxrest((1,2),(3,4)), (-2,-2))
        self.assertAlmostEqual(lc.cplxrest((5,6),(2,3)), (3,3))
    
    def test_complexdiv(self):
        self.assertAlmostEqual(lc.cplxdiv((1,2),(3,4)), (0.44,0.08))
        self.assertAlmostEqual(lc.cplxdiv((5,6),(2,3)), (2.1538461538461537, -0.23076923076923078))
    
    def test_complexmod(self):
        self.assertAlmostEqual(lc.cplxmod((1,2)), 2.23606797749979)
        self.assertAlmostEqual(lc.cplxmod((5,6)), 7.810249675906654)

    def test_complexfase(self):
        self.assertAlmostEqual(lc.cplxfase((1,2)), 1.1071487177940904)
        self.assertAlmostEqual(lc.cplxfase((5,6)), 0.8760580505981934)

    def test_complexconj(self):
        self.assertAlmostEqual(lc.cplxconj((1,2)), (1,-2))
        self.assertAlmostEqual(lc.cplxconj((5,6)), (5,-6))

    def test_polcplx(self):
        self.assertAlmostEqual(lc.polcplx((3, math.pi/4)), (2.121320343559643, 2.121320343559643))
        self.assertAlmostEqual(lc.polcplx((4, math.pi/3)), (2.0000000000000004, 3.4641016151377544))

    def test_cplxpol(self):
        self.assertAlmostEqual(lc.cplxpol((1,2)), (2.23606797749979, 1.1071487177940904))
        self.assertAlmostEqual(lc.cplxpol((5,6)), (7.810249675906654, 0.8760580505981934))

if __name__ == '__main__':
    unittest.main()