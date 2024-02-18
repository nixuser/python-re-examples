import unittest
import doctest
import word_bundary

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(word_bundary))
    return tests
