
doSomething()

function doSomething(){
    for(var i = 1;i <= 3;i+=1){
        //console.log(i);
    }
    console.log(i) 
}
console.log(i) // don't show anything
// var are limited to the function scope

// if you use the var in the global scope it will 
// change the browsers window properties so don't 
// use the var outside the function 
// var name = 'bro'
// let name = 'bro'