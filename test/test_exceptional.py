import unittest
import sys
sys.path.append("..")
from operational_steps import count_steps
from piglatin import get_piglatin
class ExceptionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("../output_exception_revised.txt","w") as f:
            pass
    def test_error_type(self):
        try:
            count_steps(45)
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestErrorType=True\n")
                print("TestErrorType =Passed ")
        except ValueError:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestErrorType=False\n")
                print("TestErrorType = Failed")
    def test_error_type_for_piglatin(self):
        try:
            get_piglatin("23")
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestErrorTypeForPiglatin=True\n")
                print("TestErrorTypeForPiglatin =Passed ")
        except ValueError:
            with open("../output_exception_revised.txt","a") as f:
                f.write("TestErrorTypeForPiglatin=False\n")
                print("TestErrorTypeForPiglatin =Failed ")
