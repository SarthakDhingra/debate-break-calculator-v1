#! usr/bin/env node

class Tournament{
    constructor(style, verbose=false) {
        this.verbose = verbose;
        this.style = style;
        this.round_point_max = style -1;
    }

    get_break(teams, breaking, rounds) {

        // edge case where all teams break
        if (teams <= breaking) {
            return "All Teams Break", "All Teams Break" // I should change this to a negative value (maybe maximum negative value) and create a hash for the form string outpu
        }
        
        // tournament point max for a team 
        let max_points = rounds * this.round_point_max;

        // create tournament TODO: (should change this t)

        let test = Array(rounds).keys();

    }
}


function get_results() {
    console.log("getting results");
}

if (require.main === module) {
    get_results();
    tournament = new Tournament(2);
    tournament.get_break(12, 8, 4);

}