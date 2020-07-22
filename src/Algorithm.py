#!/usr/bin/env python3

import numpy as np
np.set_printoptions(linewidth=300)

class TwoTeams:

    def __init__(self, verbose=False):
        self.verbose = verbose

    def getBreak(self, num_teams, num_rounds, num_breaking):
        print("got break")
        return None

class FourTeams:

    def __init__(self, verbose=False):
        print("VERBOSE")
        print(verbose)
        self.verbose = verbose

    def getBreak(self, teams, rounds, breaking):
        # come up with better name for 2d array
        max_points = rounds*3

        # each row represents a round
        # each column represents the number of points
        # rounds are indexed from 0 (i.e. row 0 = round 1)
        # points start at 0
        # each value represents the number of teams after round (row #) on the column number of points
        data = [[0 for i in range(max_points+1)] for i in range(rounds)]
        
        self.fill_data(data, rounds, teams)
        
        if self.verbose:
            print(np.array(data))
        
        teams_broken = 0
        final_teams = data[-1]
        #todo need to handle case where min_point is not assigned
        min_points = False
        for point in reversed(range(len(final_teams))):
            teams_broken += final_teams[point]
            if teams_broken >= breaking:
                min_points = point
                break


        # TO DO
        # calculate minimum # of teams to break and that percentage
        # maybe have a different method to create the matrix, then can test that too?
        return min_points
    
    def fill_data(self, data, rounds, teams):

         # ASSUMPTION that there is always at least one round
        for i in range(4):
            data[0][i] = teams / 4

        # # starting from round 2
        for round in range(1, rounds):
            round_max = (round+1)*3
            for point in range(round_max+1):
                teams = 0
                if point == 0:
                    teams = data[round-1][0] / 4
                else: 
                    for child in range(point-3,point+1):
                        if child < 0:
                            continue
                        teams += data[round-1][child] / 4
                
                data[round][point] = teams



    # TODO
    # get percentage breaking on break point
    # get # on break path
    # 
        


        