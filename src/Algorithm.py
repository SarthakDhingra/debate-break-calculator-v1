#!/usr/bin/env python3

class TwoTeams:

    def __init__(self, verbose=False):
        self.verbose = verbose

    def getBreak(self, num_teams, num_rounds, num_breaking):
        print("got break")
        return None

class FourTeams:

    def __init__(self, verbose=False):
        self.verbose = verbose

    def getBreak(self, num_teams, num_rounds, num_breaking):
        # come up with better name for 2d array
        max_points = num_rounds*3
        data = [[0 for i in range(max_points)] for i in range(num_rounds)]
        