#!/usr/bin/env node

// NOMENCLATURE:
// break: advance to outrounds
// guranteed break point: all teams on this point will break
// speaks break: some teams will break on this point


class Tournament{
    constructor(style, verbose=false) {
        this.verbose = verbose;
        this.style = style;
        this.round_point_max = style -1;
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
            console.log(round);
        }

        return ["RESULTS", "ARRAY"]

    }
}

function get_results() {
    console.log("getting results");
}

module.exports = Tournament;