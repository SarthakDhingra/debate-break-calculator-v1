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
        self.verbose = verbose

    def get_tournament(teams,breaking,rounds):

        if rounds < 1 or rounds > 9:
            raise ValueError('bad rounds')
        
        if breaking % 4 != 0:
            raise ValueError('bad break')

        if teams <= breaking:
            return "All teams break"

        # make teams divisible by 4
        while(teams%4 != 0):
            teams += 1
        
        tournament_best = [0 for i in range(teams)]
        tournament_worst = [0 for i in range(teams)]

        for round in range(rounds):
            for team in in range(0,teams,4):
                
                # pull ups lose
                tournament_best[team+1] += 1
                tournament_best[team+2] += 2
                tournament_best[team+3] += 3

                # pull ups win
                tournament_worst[team] += 3
                tournament_worst[team+1] += 2
                tournament_worst[team+2] += 3

            tournament_best.sort()
            tournament_worst.sort()
        
        results = {}
        results['best'] = get_results(tournament=tournament_best,number_teams=teams,number_breaking=breaking)
        results['worst'] = get_results(tournament=tournament_worst,number_teams=teams,number_breaking=breaking)

        return results

    def get_results(tournament,number_teams,number_breaking):
        i = len(tournament)
        

        while i >= 0:

        # WANT
        # Guranteed Break Point "guranteed_break"
        # Break Point "break_speaks"
        # number breaking on break point "breaking_speaks"
        # total on break point "total_break_point"

        #TWO CASES
        # CASE 1
        # last breaking team is guranteed break
        # CASE 2
        # last breaking team breaks on speaks

        #

        # results = {}
        # i = teams-breaking
        # breaking_point = tournament[i]

        # # CASE 1
        # if breaking_point > tournament[i-1]:
        #     results['guranteed_break'] = breaking_point
        #     results['speaks_break'] = tournament[i-1]
        #     results['breaking_on_speaks'] = 0
        #     results['total_on_speaks'] = self.get_count(tournament,i-1,left=True)
        # else:
        #     results['speaks_break'] = tournament[i]
        #     results['breaking_on_speaks'] = 



        


        # return results  


        
    def get_count(tournament,index,left=False,right=False):

        

        
        
        

        
            




        



        


        