#!/usr/bin/env python3

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../src/")

from Algorithm import Tournament

class AlgorithmTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.FourTeams = Tournament(style=4, verbose=cls.verbose)
        cls.TwoTeams = Tournament(style=2, verbose=cls.verbose)
    
    def run_given_test(self, style, test, answer):
        
        if style == 4:
            results_best,results_worst = self.FourTeams.get_Break(teams=test["teams"], breaking=test["breaking"],rounds=test["rounds"])
        else:
            results_best,results_worst = self.TwoTeams.get_Break(teams=test["teams"], breaking=test["breaking"],rounds=test["rounds"])
        
        if self.verbose:
            print("RESULTS\n")
            print(f"EXPECTED = {answer}")
            print(f"RESULTS BEST = {results_best}")
            print(f"RESULTS WORST = {results_worst}\n")

        self.assertLessEqual(results_best["guranteed_break"], answer["guranteed_break"],f"\nFAIL RESULT BEST GURANTEED\n Expected: {answer}\n Result:{results_best}")
        self.assertLessEqual(results_best['speaks_break'], answer["speaks_break"],f"\nFAILRESULT BEST SPEAKS\n Expected: {answer}\n Result:{results_best}")
        if results_best['speaks_break'] == answer["speaks_break"]:
            self.assertLessEqual(answer["breaking_on_speaks"], results_best["breaking_on_speaks"], f"\nFAIL RESULT BEST\n Expected: {answer}\n Result:{results_best}")
        
        self.assertGreaterEqual(results_worst["guranteed_break"], answer["guranteed_break"],f"\nFAIL RESULT WORST GURANTEED\n Expected: {answer}\n Result:{results_worst}")
        self.assertGreaterEqual(results_worst['speaks_break'], answer["speaks_break"],f"\nFAIL RESULT WORST SPEAKS\n Expected: {answer}\n Result:{results_worst}")
        if results_worst['speaks_break'] == answer["speaks_break"]:
            self.assertGreaterEqual(answer["breaking_on_speaks"], results_worst["breaking_on_speaks"], f"\nFAIL RESULT WORST\n Expected: {answer}\n Result:{results_worst}")
    
    def test_ubciv_2019(self):
        test = {"teams":40,"breaking":8,"rounds":5}
        answer = {"guranteed_break":11, "speaks_break":10, "breaking_on_speaks":2}
        self.run_given_test(4,test,answer)
    
    def test_hugill_2019(self):
        test = {"teams":32,"breaking":8,"rounds":5}
        answer = {"guranteed_break":10, "speaks_break":9, "breaking_on_speaks":1}
        self.run_given_test(4,test,answer)
    
    def test_hhiv_2018(self):
        test = {"teams":101,"breaking":16,"rounds":5}
        answer = {"guranteed_break":11, "speaks_break":10, "breaking_on_speaks":3}
        self.run_given_test(4,test,answer)
    
    def test_wudc_2019(self):
        test = {"teams":267,"breaking":48,"rounds":9}
        answer = {"guranteed_break":18, "speaks_break":17, "breaking_on_speaks":16}
        self.run_given_test(4,test,answer)
    
    @unittest.expectedFailure
    def test_cpnats_2018(self):
        test = {"teams":28,"breaking":8,"rounds":6}
        answer = {"guranteed_break":5, "speaks_break":5, "breaking_on_speaks":4}
        self.run_given_test(2,test,answer)
    
    def test_cpproam_2018(self):
        test = {"teams":12,"breaking":4,"rounds":4}
        answer = {"guranteed_break":4, "speaks_break":3, "breaking_on_speaks":4}
        self.run_given_test(2,test,answer)
    
    def test_cpproam_2019(self):
        test = {"teams":14,"breaking":4,"rounds":4}
        answer = {"guranteed_break":4, "speaks_break":3, "breaking_on_speaks":3}
        self.run_given_test(2,test,answer)
    
    def test_australs_2020(self):
        test = {"teams":24,"breaking":8,"rounds":4}
        answer = {"guranteed_break":3, "speaks_break":2, "breaking_on_speaks":1}
        self.run_given_test(2,test,answer)
    
    def test_mcgoun_2019(self):
        test = {"teams":12,"breaking":4,"rounds":5}
        answer = {"guranteed_break":4, "speaks_break":3, "breaking_on_speaks":3}
        self.run_given_test(2,test,answer)
    
    def test_cpnats_2020(self):
        test = {"teams":23,"breaking":8,"rounds":6}
        answer = {"guranteed_break":4, "speaks_break":3, "breaking_on_speaks":1}
        self.run_given_test(2,test,answer)
    
    def test_wudc_2020(self):
        test = {"teams":353,"breaking":48,"rounds":9}
        answer = {"guranteed_break":18, "speaks_break":17, "breaking_on_speaks":6}
        self.run_given_test(4,test,answer)

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






