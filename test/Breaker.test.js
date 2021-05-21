const Tournament = require('./../Breaker.js')

const FourTeams = new Tournament(4);
const TwoTeams = new Tournament(2);


function checkAnswer(style, test, answer) {

    let tournament = style == 4 ? FourTeams : TwoTeams

    results = tournament.getBreak(teams=test["teams"], breaking=test["breaking"],rounds=test["rounds"])
    
    let results_best = results[0]
    let results_worst = results[1]

    console.log("RESULTS\n");
    console.log(`EXPECTED = ${answer}`)
    console.log(`RESULTS BEST = ${results_best}`)
    console.log(`RESULTS WORST = ${results_worst}`)

    // make sure answer is bounded by best results
    expect(results_best["guranteed_break"]).toBeLessThanOrEqual(answer["guranteed_break"]);
    expect(results_best['speaks_break']).toBeLessThanOrEqual(answer["speaks_break"]);
    if (results_best['speaks_break'] === answer["speaks_break"]) {
        expect(answer["breaking_on_speaks"]).toBeLessThanOrEqual(results_best["breaking_on_speaks"]);
    }
    
    // make sure answer is bounded by worst results
    expect(results_worst["guranteed_break"]).toBeGreaterThanOrEqual(answer["guranteed_break"]);
    expect(results_worst['speaks_break']).toBeGreaterThanOrEqual(answer["speaks_break"]);
    if (results_worst['speaks_break'] === answer["speaks_break"]) {
        expect(answer["breaking_on_speaks"]).toBeGreaterThanOrEqual(results_worst["breaking_on_speaks"]);
    }

}

test('ubciv_2019', () => {
    let test = {"teams":40,"breaking":8,"rounds":5}
    let answer = {"guranteed_break":11, "speaks_break":10, "breaking_on_speaks":2}
    let style = 4;
    checkAnswer(style, test, answer);
});