

app.component('break-form', {
    template:
    /*html*/
    `
    <form class='break-form' @submit.prevent="onSubmit">
        <h3> This is the Form</h3>
        <label for="teams">Number of TeamsS</label>
        <input id="teams">
        <label for="rounds">Number of Preliminary Rounds </label>
        <input id="rounds">
        <label for="breaking">Number Advancing to Outrounds</label> 
        <input id="breaking">

        <input class="button" type="submit" value="Submit">  
        <input class="button" type="submit" value="Submit">  
    </form>


    `,

    methods: {
        onSubmit() {
            console.log("TESTING")
        }
    }
})