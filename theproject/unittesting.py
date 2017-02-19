import unittest
import US04

class testCase(unittest.TestCase):
    def test_same(self,):
        for j,i in US04.divdate:
            divvy=US04.divdate[i]
            marry=US04.mardate[j]
            self.assertNotEqual(divvy,marry)

    def test_almostSame(self):
        for j,i in US04.divdate:
            divvy=US04.divdate[i]
            marry=US04.mardate[i]
            self.assertAlmostEqual(divvy,marry)
    def test_less(self,):
        for j,i in US04.divdate:
            divvy=US04.divdate[i]
            marry=US04.mardate[i]
            assert divvy<marry

    def test_DnullNot(self,):
        for j,i in US04.divdate:
            divvy=US04.divdate[i]
            marry=US04.mardate[i]
            assert divvy!='null'

    def test_MnullNot(self,):
        for j,i in US04.divdate:
            divvy=US04.divdate[i]
            marry=US04.mardate[i]
            assert marry!='null'
            
if __name__=='__main__':
    unittest.main()
