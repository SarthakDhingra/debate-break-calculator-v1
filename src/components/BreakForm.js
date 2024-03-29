

app.component('break-form', {
    template:
    /*html*/
    `
    <div class="child">
        <form class="pure-form pure-form-stacked splash-subhead" @submit.prevent="onSubmit($event)">
            <label for="teams">TEAMS</label>
            <input id="teams" v-model.number="teams">
            <br>
            <label for="rounds">ROUNDS</label>
            <input id="rounds" v-model.number="rounds">
            <br>
            <label for="breaking">BREAKING</label> 
            <input id="breaking" v-model.number="breaking">
            <br>
            <button class="pure-button" name="style" value=2 type="submit">Two Teams</button>
            <button class="pure-button" name="style" value=4 type="submit">Four Teams</button> 
        </form>
    </div>

    <div v-if="displayResults" class="splash-subhead grandchild">
        <table>
            <tr>
                <th>BEST CASE</th>
                <th>WORST CASE</th>
            </tr>
            <tr>
                <td>{{best_string}}</td>
                <td>{{worst_string}}</td>
            </tr>
        </table>
    </div>

    `,
    data() {
        return {
            teams: 40,
            rounds: 5,
            breaking: 8,
            displayResults: false,
            best_string: '',
            worst_string: ''
        }
    },
    methods: {
        onSubmit(event) {

            let style = event.submitter.attributes.value.value
            let results = this.getResults(style, this.teams, this.breaking, this.rounds)
            console.log("RESULTS")
            let best = results[0]
            let worst = results[1]

            console.log(best)
            console.log(worst)
            this.best_string = `All teams on ${best.guranteed_break} points will break. ${best.breaking_on_speaks} out of ${best.total_on_speaks} teams on ${best.speaks_break} points will break`
            this.worst_string = `All teams on ${worst.guranteed_break} points will break. ${worst.breaking_on_speaks} out of ${worst.total_on_speaks} teams on ${worst.speaks_break} points will break`
            this.displayResults = true
        }
    }
})

