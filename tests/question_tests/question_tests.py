#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_assessment_value, get_tax_assessed, test_config
from src.question_b.question_b import get_sum_of_evens
from src.question_c.question_c import get_person_category
from src.question_d.question_d import use_local_variable


class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_assessment_value(self):
        self.assertEqual(get_assessment_value(10000), 6000)
        self.assertEqual(get_assessment_value(20000), 12000)

    def test_get_tax_assessed(self):
        self.assertEqual(get_tax_assessed(6000), 43.20)
        self.assertEqual(get_tax_assessed(10000), 72)

    def test_get_sum_of_evens(self):
        self.assertEqual(get_sum_of_evens(11), 30)
        self.assertEqual(get_sum_of_evens(10), 30)
        self.assertEqual(get_sum_of_evens(8), 20)
    
    def test_get_person_category(self):
        self.assertEqual(get_person_category(1), "Infant")
        self.assertEqual(get_person_category(2), "Child")
        self.assertEqual(get_person_category(14), "Teenager")
        self.assertEqual(get_person_category(20), "Adult")


    def test_use_local_variable(self):
        num = 100
        use_local_variable(num)
        self.assertEqual(num, 100)