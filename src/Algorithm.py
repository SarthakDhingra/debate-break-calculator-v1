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

        # each row represents a round
        # each column represents the number of points
        # rounds are indexed from 0 (i.e. row 0 = round 1)
        # points start at 0
        # each value represents the number of teams after round (row #) on the column number of points
        data = [[0 for i in range(max_points+1)] for i in range(num_rounds)]

        # ASSUMPTION that there is always at least one round
        for i in range(3):
            data[0][i] = max_points / 4

        # # starting from round 2
        for round in range(1, rounds):
            round_max = (round+1)*3
            for point in range(round_max):
                teams = 0
                if point == 0:
                    teams = data[round-1][0] / 4
                else: 
                    for child in range(point-3,point+1):
                        if child < 0:
                            continue
                        teams += data[round-1][child] / 4
                
                data[round][point] = teams

        # TO DO
        # calculate minimum # of teams to break and that percentage
        return None
        