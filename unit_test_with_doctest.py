import unittest
import doctest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocFileSuite("re_examples.md"))
    return tests

