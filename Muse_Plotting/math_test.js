
function firstTask() {

    //Math.floor creats only integers
    x = Math.floor(Math.random() * 100);
    y = Math.floor(Math.random() *100);
    problem = x + "+" +  y;
    
    document.getElementById("demo").innerHTML = problem;

}


function task() {

    var x = Math.floor(Math.random() * 100);
    var y = Math.floor(Math.random() * 100);
    var problem = x + "+" + y ;
    
    document.getElementById("demo").innerHTML = problem;
}