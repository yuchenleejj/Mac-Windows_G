let userName = "";
// null is equal to none
// in this situation this null means u can leave with cancel button
while(userName == ""||userName == null){
    userName = window.prompt("Enter your name:")
}

console.log("Hello",userName)

// while(1==1){
//     console.log("I'm stuck in an infinite loop!")
// }



// do something first and then check the condition
let userName1 ;
do{
    userName1 = window.prompt("Enter your name:")
}while(userName1 == '')