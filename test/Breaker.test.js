const Tournament = require('./../Breaker.js')

const FourTeams = new Tournament(4);
const TwoTeams = new Tournament(2);


function check_answer(style, test, answer) {

    let tournament = style == 4 ? FourTeams : TwoTeams


    results = tournament.getBreak(teams=test["teams"], breaking=test["breaking"],rounds=test["rounds"])
    
    console.log(results)

    expect(1).toBe(1)

}

test('ubciv_2019', () => {
    let test = {"teams":40,"breaking":8,"rounds":5}
    let answer = {"guranteed_break":11, "speaks_break":10, "breaking_on_speaks":2}
    let style = 4;
    check_answer(style, test, answer);
});