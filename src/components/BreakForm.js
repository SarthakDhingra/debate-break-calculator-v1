

app.component('break-form', {
    template:
    /*html*/
    `
    <form class='break-form' @submit.prevent="onSubmit($event)">
        <h3> This is the Form</h3>
        <label for="teams">Number of TeamsS</label>
        <input id="teams" v-model.number="teams" >
        <label for="rounds">Number of Preliminary Rounds </label>
        <input id="rounds" v-model.number="rounds">
        <label for="breaking">Number Advancing to Outrounds</label> 
        <input id="breaking" v-model.number="breaking">

        <button name="style" value=2 type="submit">Two Teams</button>
        <button name="style" value=4 type="submit">Four Teams</button> 
    </form>

    <div v-if="displayResults">
        <table style="width:100%">
            <tr>
                <th>Best Case Scenario</th>
                <th>Worst Case Scenario</th>
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
            teams: null,
            rounds: null,
            breaking: null,
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


            // <h1 v-if="awesome">Vue is awesome!</h1>
        }
    }
})