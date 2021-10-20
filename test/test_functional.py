import colorama
from colorama import Fore
colorama.init(autoreset=True)
import unittest
import sys
sys.path.append("..")
from operational_steps import count_steps
from piglatin import get_piglatin
class FuctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("output_revised.txt","w") as f:
            pass
    def test_return_type_int(self):
        n=count_steps(25)
        if type(n)==type(1):
            with open("output_revised.txt","a") as f:
                f.write("TestReturnTypeInt=True\n")
                print("{}TestReturnTypeInt = {}Passed".format(Fore.YELLOW,Fore.GREEN))
        else:
            with open("output_revised.txt","a") as f:
                f.write("TestReturnTypeInt=False\n")
                print("{}TestReturnTypeInt = {}Failed".format(Fore.YELLOW,Fore.RED))
    def test_return_type_for_piglatin(self):
        s=get_piglatin("This is Venu")
        if type(s)==type(" "):
            with open("output_revised.txt","a") as f:
                f.write("TestReturnTypeForPiglatin=True\n")
                print("{}TestReturnTypeForPiglatin = {}Passed".format(Fore.YELLOW,Fore.GREEN))
        else:
            with open("output_revised.txt","a") as f:
                f.write("TestReturnTypeForPiglatin=False\n")
                print("{}TestReturnTypeForPiglatin = {}Failed".format(Fore.YELLOW,Fore.RED))
