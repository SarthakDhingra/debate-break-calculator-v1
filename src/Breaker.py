#!/usr/bin/env python3

import numpy as np
from math import floor, ceil
np.set_printoptions(linewidth=300)

# ASSUMPTIONS:
# Tournament is bracketed

class Tournament:
    def __init__(self, style, verbose=False):
        self.verbose = verbose
        self.style = style
        self.round_point_max = style-1

    def get_Break(self,teams,breaking,rounds,convert_string=False):

        if teams <= breaking:
            return "All Teams Break", "All Teams Break"

        # max points a team can get in the tournament
        max_points = rounds*(self.round_point_max)

        # simulate tournament
        tournament = [[0 for i in range(max_points+1)] for i in range(rounds)]
        self.fill_data(tournament, rounds, teams)

        if self.verbose:
            print(np.array(tournament))
        
        # get best and worst case break results
        results_best = self.get_results(tournament=tournament[-1], teams=teams, breaking=breaking, case="BEST")
        results_worst = self.get_results(tournament=tournament[-1], teams=teams, breaking=breaking, case="WORST")

        if convert_string:
            results_best = f"All teams on {results_best.get('guranteed_break')} points will break. {results_best.get('breaking_on_speaks')} out of \
            {results_best.get('total_on_speaks')} teams on {results_best.get('speaks_break')} points will break"
            results_worst = f"All teams on {results_worst.get('guranteed_break')} points will break. {results_worst.get('breaking_on_speaks')} out of \
            {results_worst.get('total_on_speaks')} teams on {results_worst.get('speaks_break')} points will break"
          
        return results_best, results_worst
    
    def fill_data(self, tournament, rounds, teams):
        # Simulate a tournament (2D array) where:
            # a row represents the round (.e. row 0 is round 1, row 1 is round 2, etc.)
            # a column represents a point number (column 0 = 0 points, column 1 = 1 point, etc.)
            # a cell value represents the number of teams after that round (row # + 1) on column number of points 
            # (i.e. tournament[3][5] represents the number of teams after round 3 on 5 points)
        
        # simulate round 1
        for i in range(self.style):
            tournament[0][i] = teams / self.style

        # simulate rest of tournament
        for round in range(1, rounds):
            round_max = (round+1)*self.round_point_max
            for point in range(round_max+1):
                teams = 0
                if point == 0:
                    teams = tournament[round-1][0] / self.style
                else: 
                    for child in range(point-self.round_point_max,point+1):
                        if child < 0:
                            continue
                        teams += tournament[round-1][child] / self.style
                tournament[round][point] = teams

    def get_results(self, tournament, teams, breaking, case):
        
        if self.verbose:
            print(f"TOURANEMNT={tournament}")
        
        
        results = {} 
        point = len(tournament)-1
        # counter for total teams that have succesfully broken
        teams_broke = 0 
        # counter for total teams that have succesfully broken on the guranteed break point or higher
        teams_broke_prev = 0

        while teams_broke < breaking:
            teams_broke_prev = teams_broke
            if case == "WORST":
                teams_broke += ceil(tournament[point])
            elif case == "BEST":
                teams_broke += floor(tournament[point])
            point-=1

        breaking_on_speaks = breaking - teams_broke_prev
        total_on_speaks = ceil(tournament[point+1])
        
        if breaking_on_speaks == total_on_speaks:
            point -= 1
            breaking_on_speaks = 0
            total_on_speaks = ceil(tournament[point+1])

        results['speaks_break'] = point + 1
        results['guranteed_break'] = point + 2
        results['breaking_on_speaks'] = breaking_on_speaks
        results['total_on_speaks'] = total_on_speaks

        return results


        

        
        
        

        
            




        



        


        