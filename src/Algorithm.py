#!/usr/bin/env python3

import numpy as np
np.set_printoptions(linewidth=300)

class Tournament:

    def __init__(self, style, verbose=False):
        self.verbose = verbose
        self.style = style
        self.team_map = {0:3,1:2,2:1} if self.style == 4 else {0:1}

    def get_Break(self,teams,breaking,rounds,convert_string=False):

        if teams <= breaking:
            return "All Teams Break", "All Teams Break"

        # make teams divisible by 4
        while(teams% self.style != 0):
            teams += 1
        
        tournament_best = [0 for i in range(teams)]
        tournament_worst = [0 for i in range(teams)]

        for round in range(rounds):
            for team in range(0,teams):
                if (team % self.style == 0):
                    for i in range(1,self.style):
                        tournament_best[team+i] += i
                        tournament_worst[team + i - 1] += self.team_map[i-1]

            tournament_best.sort()
            tournament_worst.sort()

        if self.verbose:
            print(f"TOURNAMENT BEST = {tournament_best}")
            print(f"TOURNAMENT WORST = {tournament_worst}")
        
        results_best = self.get_results(tournament=tournament_best,teams=teams,breaking=breaking)
        results_worst = self.get_results(tournament=tournament_worst,teams=teams,breaking=breaking)

        if convert_string:
            results_best = f"All teams on {results_best.get('guranteed_break')} points will break. {results_best.get('breaking_on_speaks')} out of {results_best.get('total_on_speaks')} teams on {results_best.get('speaks_break')} points will break"
            results_worst = f"All teams on {results_worst.get('guranteed_break')} points will break. {results_worst.get('breaking_on_speaks')} out of {results_worst.get('total_on_speaks')} teams on {results_worst.get('speaks_break')} points will break"
          

        return results_best, results_worst

    def get_results(self,tournament,teams,breaking):
        break_index = len(tournament) - breaking

        points = []
        results = {}

        for i in range(-breaking,1):
            if len(points) == 2:
                break
            if tournament[i] not in points:
                points.append(tournament[i])
        
        # can probably simplify this
        if len(points) == 1:
            if tournament[break_index-1] < tournament[break_index]:
                points = [tournament[break_index], points[0]]
            else:
                points = [points[0],"No Guranteed Break"]
        elif tournament[break_index-1] < tournament[break_index]:
            points = [tournament[break_index-1], tournament[break_index]]

        results['speaks_break'] = points[0]
        results['guranteed_break'] = points[1]

        # bug if there is no guranteed break point
        num_speaks_break = 0
        i = break_index
        while i < len(tournament) and results['speaks_break'] == tournament[i]:
            i += 1
            num_speaks_break += 1
        results['breaking_on_speaks'] = num_speaks_break

        total_speaks_break = 0
        i = break_index-1
        while i >= 0  and tournament[i] == results['speaks_break']:
            i += 1
            total_speaks_break += 1
        
        results['total_on_speaks'] = total_speaks_break + num_speaks_break

        return results




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


        

        
        
        

        
            




        



        


        