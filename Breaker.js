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

        this.fillData(tournament, rounds, teams);

        console.log("TOURNAMENT FILLED")
        for (let i = 0; i < tournament.length; i++ ) {
            console.log(tournament[i])
        }

        return ["RESULTS", "ARRAY"]

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
                        teams += tournament[round-1][child] / self.style
                    }                        
                }
                tournament[round][point] = teams
            }
        }
    }


}

function get_results() {
    console.log("getting results");
}



module.exports = Tournament;