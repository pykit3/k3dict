import doctest

import k3dictutil


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(k3dictutil))
    return tests
