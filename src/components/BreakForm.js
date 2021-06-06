

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

        <button name="style" value=2 type="submit" v-bind="style">Two Teams</button>
        <button name="style" value=4 type="submit" v-bind="style">Four Teams</button> 
    </form>


    `,
    data() {
        return {
            teams: 40,
            rounds: 5,
            breaking: 8,
        }
    },
    methods: {
        onSubmit(event) {

            console.log("TESTING")
            let style = event.submitter.attributes.value.value
            console.log(style) // 4
            console.log(this.teams) // 40
            console.log(this.rounds) // 5
            console.log(this.breaking) // 8
            let results = this.getResults(style, this.teams, this.breaking, this.rounds)
            console.log("RESULTS")
            console.log(results)
        }
    }
})