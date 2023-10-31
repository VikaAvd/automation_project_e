import unittest
import sys
import os

"""
Loading and running tests
https://docs.python.org/2/library/unittest.html#loading-and-running-tests
https://docs.python.org/3.10/library/unittest.html#loading-and-running-tests
How do I run all Python unit tests in a directory?
https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory
"""

tests_dir = os.path.join(os.path.dirname(__file__), "tests")
print("tests_dir" , tests_dir)
sys.path.append(tests_dir)

test_loader = unittest.TestLoader()
test_suite = test_loader.discover(tests_dir)

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(test_suite)