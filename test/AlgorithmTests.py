#!/usr/bin/env python3

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../src/")

from Algorithm import TwoTeams, FourTeams

class AlgorithmTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.four_teams = FourTeams(verbose=cls.verbose)
        cls.two_teams = TwoTeams(verbose=cls.verbose)
    
    def run_four_teams(self, test, answer):
        result = self.four_teams.getBreak(teams=test["teams"], breaking=test["breaking"],rounds=test["rounds"])
        print(result)
        self.assertEqual(result,answer,f"FAIL\n Expected = {answer}, result={result}")
    
    def test_temp(self):
        test = {"teams":30,"breaking":8,"rounds":5}
        answer = {"min_points":9, "breaking_on_break_point":38}
        self.run_four_teams(test,answer)

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description="Calculate Debate Breaks")
    parser.add_argument('-t', help="test name", default=None, dest="test_name", action="store")
    parser.add_argument('-v', help="extra logs", default=None, dest="verbose", action="store_true")

    args = parser.parse_args()

    AlgorithmTests.verbose = args.verbose

    if args.test_name is None:
        unittest.main()
    else:
        test_name = "test_{0}".format(args.test_name)
        suite = unittest.TestSuite()
        suite.addTest(AlgorithmTests(test_name))
        runner = unittest.TextTestRunner()
        runner.run(suite)






