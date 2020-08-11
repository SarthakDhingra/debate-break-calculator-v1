#!/usr/bin/env python3

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../src/")

from Algorithm import FourTeams

class AlgorithmTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.four_teams = FourTeams(verbose=cls.verbose)
    
    def run_four_teams(self, test, answer):
        results_best,results_worst = self.four_teams.get_Break(teams=test["teams"], breaking=test["breaking"],rounds=test["rounds"])
        
        # Guranteed Break Point "guranteed_break"
        # Break Point "break_speaks"
        # number breaking on break point "breaking_speaks"
        # total on break point "total_break_point"

        #give --> break point, number breaking on that point, total breaking on that point, guranteed break
        self.assertLessEqual(results_best["guranteed_break"], answer["guranteed_break"],f"FAIL\n Expected: {answer}\n Result:{results_best}")
        self.assertLessEqual(results_best['speaks_break'], answer["speaks_break"],f"FAIL\n Expected: {answer}\n Result:{results_best}")
        if results_best['speaks_break'] == answer["speaks_break"]:
            self.assertLessEqual(results_best["breaking_on_speaks"], answer["breaking_on_speaks"],f"FAIL\n Expected: {answer}\n Result:{results_best}")
        
        self.assertGreaterEqual(results_worst["guranteed_break"], answer["guranteed_break"],f"FAIL\n Expected: {answer}\n Result:{results_worst}")
        self.assertGreaterEqual(results_worst['speaks_break'], answer["speaks_break"],f"FAIL\n Expected: {answer}\n Result:{results_worst}")
        if results_worst['speaks_break'] == answer["speaks_break"]:
            self.assertGreaterEqual(results_best["breaking_on_speaks"], answer["breaking_on_speaks"],f"FAIL\n Expected: {answer}\n Result:{results_worst}")
    
    def test_ubciv_2019(self):
        test = {"teams":40,"breaking":8,"rounds":5}
        answer = {"guranteed_break":11, "speaks_break":10, "breaking_on_speaks":2}
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






