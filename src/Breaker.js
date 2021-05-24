#!/usr/bin/env node

// NOMENCLATURE:
// break: advance to outrounds
// guranteed break point: all teams on this point will break
// speaks break: some teams will break on this point


class Tournament{
    constructor(style, verbose=false) {
        this.verbose = verbose;
        this.style = style;
        this.round_point_max = style - 1;
    }

    getBreak(teams, breaking, rounds) {

        // edge case where all teams break
        if (teams <= breaking) {
            return "All Teams Break", "All Teams Break" // I should change this to a negative value (maybe maximum negative value) and create a hash for the form string outpu
        }
        
        // tournament point max for a team 
        let max_points = rounds * this.round_point_max;

        // create tournament TODO: (should change this)

        const tournament = [];

        for (let i = 0; i < rounds; i++) {
            const round = new Array(max_points + 1).fill(0);
            tournament.push(round);
        }

        //console.log("TOURNAMENT 1:")
        for (let i = 0; i < tournament.length; i++ ) {
            //console.log(tournament[i])
        }

        this.fillData(tournament, rounds, teams);

        //console.log("TOURNAMENT 2:")
        for (let i = 0; i < tournament.length; i++ ) {
            //console.log(tournament[i])
        }

        // get best and worst case break results TODO: better to just call getResults once and return one array with two objects
        // have while loop in its own function maybe to do this
        // or just nest in a for loop with both cases

        let results_best = this.getResults(tournament.slice(-1), breaking, "BEST")
        let results_worst = this.getResults(tournament.slice(-1), breaking, "WORST")

        return [results_best, results_worst]

    }

    fillData(tournament, rounds, teams) {
        // Simulate a tournament (2D array) where:
            // a row represents the round (.e. row 0 is round 1, row 1 is round 2, etc.)
            // a column represents a point number (column 0 = 0 points, column 1 = 1 point, etc.)
            // a cell value represents the number of teams after that round (row + 1) on column number of points 
            // (i.e. tournament[3][5] represents the number of teams after round 4 on 5 points)
        
        // simulate round 1
        for (let i=0; i < this.style; i++) {
            tournament[0][i] = teams / this.style
        }

        // simulate rest of tournament
        for (let round=1; round < rounds; round++) {
            //maximum number of points possible after this tournament
            let round_max = (round + 1 ) * this.round_point_max

            // calculate number of teams that are now on each point
            for (let point = 0; point <= round_max; point++) {
                let teams = 0
                // handle edge case of teams now on 0 points
                if (point === 0) {
                    teams = tournament[round-1][0] / this.style
                }
                // get number of teams on current round based off previous rounds
                // i.e. if the style is BP, the number of teams on 5 points will be equivalent
                // to 1/4 teams on 2 points + 1/4 teams on 3 ponts + 1/4 teams on 
                // 4 points + 1/4 teams on 5 points from the previous round
                else {
                    for (let child = point - this.round_point_max; child <= point; child++) {
                        // TODO: change conditional and get rid of continue
                        if (child < 0) {
                            continue
                        }
                        teams += tournament[round-1][child] / this.style
                    }                        
                }
                tournament[round][point] = teams
            }
        }
    }

    getResults(tournament, breaking, cases) {


        //console.log("TOURNAMENT")
        //console.log(tournament)

        let results = {}

        tournament = tournament[0]

        let point = tournament.length - 1

        // counter for total teams that have succesfully broken
        let teams_broke = 0 
        
        // counter for total teams that have succesfully broken on or above guranteed break point
        let teams_broke_prev = 0

        // descend through points adding the number of teams that have broken until break capacity is exceeded
        while (teams_broke < breaking) {
            teams_broke_prev = teams_broke
            if (cases === "WORST") {
                teams_broke += Math.ceil(tournament[point])
            } else {
                teams_broke += Math.floor(tournament[point])
            }
            point-=1
        }

        let breaking_on_speaks = breaking - teams_broke_prev
        let total_on_speaks = Math.ceil(tournament[point+1])
        
        // handle edge case where all teams on speaks break
        if (breaking_on_speaks === total_on_speaks) {
            point -= 1
            breaking_on_speaks = 0
            total_on_speaks = Math.ceil(tournament[point+1])
        }

        // fill dict with desired values
        results['speaks_break'] = point + 1
        results['guranteed_break'] = point + 2
        results['breaking_on_speaks'] = breaking_on_speaks
        results['total_on_speaks'] = total_on_speaks

        return results

    }


}

if (require.main === module) {
    let teams = 40
    let breaking = 8
    let rounds = 5

    let FourTeams = new Tournament(4)
    FourTeams.getBreak(teams, breaking, rounds)
}



module.exports = Tournament;