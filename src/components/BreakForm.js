
app.component('break-form', {
    template:
    /*html*/
    `
    <form>
        <h3> This is the Form</h3>
        <label for="teams">Number of Teams</label>
        <input id="teams">
        <label for="rounds">Number of Preliminary Rounds </label>
        <input id="rounds">
        <label for="breaking">Number Advancing to Outrounds</label> 
        <input id="breaking">
    </form>

    <input class="button" type="submit" value="Submit">  
    <input class="button" type="submit" value="Submit">  
    `
})