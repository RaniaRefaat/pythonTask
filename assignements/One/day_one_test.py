from labOnePartOneC import lab_one_part_one
from labOnePartTwo import lab_two_part_two
from lapOnePartThree import lap_one_part_three
from lapOnePartFive import lab_one_part_five
from labOnePartSix import lab_one_part_six
from labOnePartFour import calcArea

import unittest
class TestAssignmentOne(unittest.TestCase):
        def test_lab_one_part_one(self):
            self.assertEqual(lab_one_part_one('mobile'), 'mbl')
            self.assertEqual(lab_one_part_one('MOBILE'), 'MBL')
            self.assertEqual(lab_one_part_one('MobIlE'), 'Mbl')
        def test_lab_two_part_two(self):
            self.assertEqual(lab_two_part_two('This is javaScript','i'), [2,5,15])
        def test_lap_one_part_three(self):
            self.assertEqual(lap_one_part_three(3), [[1],[2,4],[3,6,9]])
        def test_task_five_haitham(self):
            l1 = ["ahmed", "fatma", "ibrahim"]
            d1 = {'a':['ahmed'], 'f':['fatma'],'i':['ibrahim']}
        def test_calcArea(self):
            self.assertEqual(calcArea('t',3,4), (6)) 
            self.assertEqual(calcArea('r',3,4), (12))
            self.assertEqual(calcArea('s',3,4), (9))   
            self.assertEqual(calcArea('c',3,4), (3.14*9))   
if __name__ == '__main__':
    unittest.main()            
