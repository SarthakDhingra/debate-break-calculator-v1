#!/usr/bin/env python3

import numpy as np
np.set_printoptions(linewidth=300)
from math import floor, ceil

class Tournament:

    # ASSUMPTIONS
    # Tournament is bracketed

    def __init__(self, style, verbose=False):
        self.verbose = verbose
        self.style = style
        self.round_point_max = style-1

    def get_Break(self,teams,breaking,rounds,convert_string=False):

        if teams <= breaking:
            return "All Teams Break", "All Teams Break"

        max_points = rounds*(self.round_point_max)

        # Simulate a tournament using a 2D matrix where:
            # each row represents the round (.e. row 0 is round 1, row 1 is round 2, etc.)
            # each column represents a number of points (column 0 = 0 points, column 1 = 1 point, etc.)
            # each cell value represents the number of teams after round (row # + 1) on column number of points 
            # (i.e. tournament[3][5] represents the number of teams after round 3 on 5 points)
        tournament = [[0 for i in range(max_points+1)] for i in range(rounds)]
        self.fill_data(tournament, rounds, teams)

        if self.verbose:
            print(np.array(tournament))
        
        # get results
        results_best, results_worst = self.get_results(tournament=tournament[-1],teams=teams,breaking=breaking)

        if convert_string:
            results_best = f"All teams on {results_best.get('guranteed_break')} points will break. {results_best.get('breaking_on_speaks')} out of \
            {results_best.get('total_on_speaks')} teams on {results_best.get('speaks_break')} points will break"
            results_worst = f"All teams on {results_worst.get('guranteed_break')} points will break. {results_worst.get('breaking_on_speaks')} out of \
            {results_worst.get('total_on_speaks')} teams on {results_worst.get('speaks_break')} points will break"
          
        return results_best, results_worst
    
    def fill_data(self, data, rounds, teams):

        for i in range(self.style):
            data[0][i] = teams / self.style

        # starting from round 2
        for round in range(1, rounds):
            round_max = (round+1)*self.round_point_max
            for point in range(round_max+1):
                teams = 0
                if point == 0:
                    teams = data[round-1][0] / self.style
                else: 
                    for child in range(point-self.round_point_max,point+1):
                        if child < 0:
                            continue
                        teams += data[round-1][child] / self.style
                
                data[round][point] = teams

    # add up all rounded up points for that round
    # the highest point while it still smaller than number breaking is guranteed break
    # the point after is the cut off
    # the number breaking from this is (x - summation of all points until guranteed break) out of R where R can be ceil or floor of cutoff number
    # have to explain why R can either or if its best case, why not ceil (because there are break cases )

    def get_results(self,tournament,teams,breaking):
        
        if self.verbose:
            print(f"TOURANEMNT={tournament}")

        #WORST CASE
        results_worst = {}

        teams_broke = 0
        teams_broke_prev = 0
        point = len(tournament)-1

        while teams_broke < breaking:
            teams_broke_prev = teams_broke
            teams_broke += ceil(tournament[point])
            point-=1
        
        results_worst['speaks_break'] = point + 1
        results_worst['guranteed_break'] = point + 2
        results_worst['total_on_speaks'] = ceil(tournament[point+1])
        results_worst['breaking_on_speaks'] = breaking - teams_broke_prev

        #BEST CASE
        results_best = {}

        teams_broke = 0
        teams_broke_prev = 0
        point = len(tournament)-1

        while teams_broke < breaking:
            teams_broke_prev = teams_broke
            teams_broke += floor(tournament[point])
            point-=1
        
        results_best['speaks_break'] = point + 1
        results_best['guranteed_break'] = point + 2
        results_best['total_on_speaks'] = ceil(tournament[point+1])
        results_best['breaking_on_speaks'] = breaking - teams_broke_prev

        return results_best, results_worst






        # break_index = len(tournament) - breaking

        # points = []
        # results = {}

        # for i in range(-breaking,1):
        #     if len(points) == 2:
        #         break
        #     if tournament[i] not in points:
        #         points.append(tournament[i])
        
        # # can probably simplify this
        # if len(points) == 1:
        #     if tournament[break_index-1] < tournament[break_index]:
        #         points = [tournament[break_index], points[0]]
        #     else:
        #         points = [points[0],"No Guranteed Break"]
        # elif tournament[break_index-1] < tournament[break_index]:
        #     points = [tournament[break_index-1], tournament[break_index]]

        # results['speaks_break'] = points[0]
        # results['guranteed_break'] = points[1]

        # # bug if there is no guranteed break point
        # num_speaks_break = 0
        # i = break_index
        # while i < len(tournament) and results['speaks_break'] == tournament[i]:
        #     i += 1
        #     num_speaks_break += 1
        # results['breaking_on_speaks'] = num_speaks_break

        # total_speaks_break = 0
        # i = break_index-1
        # while i >= 0  and tournament[i] == results['speaks_break']:
        #     i += 1
        #     total_speaks_break += 1
        
        # results['total_on_speaks'] = total_speaks_break + num_speaks_break

        # return results




    #     results = {}
    #     i = teams-breaking
    #     breaking_point = tournament[i]

    #     # no one breaks on speaks, and guranteed_break point is last breaking team
    #     if breaking_point > tournament[i-1]:
    #         results['guranteed_break'] = breaking_point
    #         results['speaks_break'] = tournament[i-1]
    #         results['breaking_on_speaks'] = 0
    #         results['total_on_speaks'] = self.get_count(tournament,i-1,left=True)
    #     else:
    #         results['speaks_break'] = tournament[i]
    #         results['breaking_on_speaks'] = 
    #         results['']

    #     return results  
    # def get_count(tournament,index,left=False,right=False):


        

        
        
        

        
            




        



        


        