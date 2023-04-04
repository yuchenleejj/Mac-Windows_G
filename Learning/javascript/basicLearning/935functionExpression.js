// function expression = function without a name (anonymous function)
//                       avoid polluting the global scope with names
//                       write it, then forget about it

let count = 0;

document.getElementById('increaseBtn').onclick = function(){
    count+=1;
    document.getElementById("myLabel").innerHTML = count;
}
document.getElementById('decreaseBtn').onclick = function(){
    count-=1;
    document.getElementById("myLabel").innerHTML = count;
}

// function decreaseCount(){
//     count-=1;
//     document.getElementById("myLabel").innerHTML = count;
// }
// function increaseCount(){
//     count+=1;
//     document.getElementById("myLabel").innerHTML = count;
// }
// mainly for some html simple function usage like: button