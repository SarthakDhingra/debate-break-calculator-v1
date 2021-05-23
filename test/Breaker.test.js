const Tournament = require('./../Breaker.js')

const FourTeams = new Tournament(4);
const TwoTeams = new Tournament(2);


function checkAnswer(style, test, answer) {

    let tournament = style == 4 ? FourTeams : TwoTeams

    results = tournament.getBreak(teams=test["teams"], breaking=test["breaking"],rounds=test["rounds"])
    
    let results_best = results[0]
    let results_worst = results[1]

    // console.log("RESULTS\n");
    // console.log(`EXPECTED = ${answer}`)
    // console.log(`RESULTS BEST = ${results_best}`)
    // console.log(`RESULTS WORST = ${results_worst}`)

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

test('hugill_2019', () => {
    let test = {"teams":32,"breaking":8,"rounds":5}
    let answer = {"guranteed_break":10, "speaks_break":9, "breaking_on_speaks":1}
    let style = 4;
    checkAnswer(style, test, answer); 
});

test('hhiv_2018', () => {
    let test = {"teams":101,"breaking":16,"rounds":5}
    let answer = {"guranteed_break":11, "speaks_break":10, "breaking_on_speaks":3}
    let style = 4;
    checkAnswer(style, test, answer); 
});

test('wudc_2019', () => {
    let test = {"teams":267,"breaking":48,"rounds":9}
    let answer = {"guranteed_break":18, "speaks_break":17, "breaking_on_speaks":16}
    let style = 4;
    checkAnswer(style, test, answer); 
});

test.skip('cpnats_2018', () => {
    let test = {"teams":28,"breaking":8,"rounds":6}
    let answer = {"guranteed_break":5, "speaks_break":5, "breaking_on_speaks":4}
    let style = 2;
    checkAnswer(style, test, answer); 
});

test.skip('cpproam_2018', () => {
    let test = {"teams":12,"breaking":4,"rounds":4}
    let answer = {"guranteed_break":4, "speaks_break":3, "breaking_on_speaks":4}
    let style = 2;
    checkAnswer(style, test, answer); 
});

test('cpproam_2019', () => {
    let test = {"teams":14,"breaking":4,"rounds":4}
    let answer = {"guranteed_break":4, "speaks_break":3, "breaking_on_speaks":3}
    let style = 2;
    checkAnswer(style, test, answer); 
});

test('australs_2020', () => {
    let test = {"teams":24,"breaking":8,"rounds":4}
    let answer = {"guranteed_break":3, "speaks_break":2, "breaking_on_speaks":1}
    let style = 2;
    checkAnswer(style, test, answer); 
});

test('mcgoun_2019', () => {
    let test = {"teams":12,"breaking":4,"rounds":5}
    let answer = {"guranteed_break":4, "speaks_break":3, "breaking_on_speaks":3}
    let style = 2;
    checkAnswer(style, test, answer); 
});

test('cpnats_2020', () => {
    let test = {"teams":23,"breaking":8,"rounds":6}
    let answer = {"guranteed_break":4, "speaks_break":3, "breaking_on_speaks":1}
    let style = 2;
    checkAnswer(style, test, answer); 
});

test('wudc_2020', () => {
    let test = {"teams":353,"breaking":48,"rounds":9}
    let answer = {"guranteed_break":18, "speaks_break":17, "breaking_on_speaks":6}
    let style = 4;
    checkAnswer(style, test, answer); 
});
