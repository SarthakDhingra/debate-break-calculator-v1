#!/usr/bin/env python3

import numpy as np
np.set_printoptions(linewidth=300)

# WORST CASE
# add up all rounded up points for that round
# the highest point while it still smaller than number breaking is guranteed break
# the point after is the cut off
# the number breaking from this is (x - summation of all points until guranteed break) out of R where R can be ceil or floor of cutoff number
# have to explain why R can either or if its best case, why not ceil (because there are break cases )

# BEST CASE
# same but with rounded down

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
        breaking_on_break_point = False
        for point in reversed(range(len(final_teams))):
            teams_broken += final_teams[point]
            if teams_broken >= breaking:
                breaking_on_break_point = ((teams_broken - breaking) / final_teams[point])*100
                min_points = point
                break


        # TO DO
        # calculate minimum # of teams to break and that percentage
        # maybe have a different method to create the matrix, then can test that too?
        return {"min_points":min_points, "breaking_on_break_point":breaking_on_break_point}
    
    def fill_data(self, data, rounds, teams):

         # ASSUMPTION that there is always at least one round
        for i in range(4):
            data[0][i] = teams / 4

        # starting from round 2
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
        


        