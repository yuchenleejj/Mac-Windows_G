// let x = Math.floor(Math.random()*6)+1; 
// // this will generate a random number from 1 to 6
// let y = Math.floor(Math.random()*6)+1; 
// let z = Math.floor(Math.random()*6)+1; 

// console.log(x);
// console.log(y);
// console.log(z);

let x;
let y;
let z;

document.getElementById("rollButton").onclick = function(){
    x = Math.floor(Math.random() * 6) + 1; 
    y = Math.floor(Math.random() * 6) + 1; 
    z = Math.floor(Math.random() * 6) + 1; 

    document.getElementById("xlabel").innerHTML = x;
    document.getElementById("ylabel").innerHTML = y;
    document.getElementById("zlabel").innerHTML = z;
}

// Don't add the parenthesis behind the onclick