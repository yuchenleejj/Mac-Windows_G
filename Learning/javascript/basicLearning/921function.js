
// startProgram();
// function startProgram(){
//     let userName = 'Justin';
//     let age = 22;
//     happyBirthday(userName,age);
// }


// function happyBirthday(userName,age){
//     console.log("Happy birthday to you!");
//     console.log("Happy birthday to you!");
//     console.log("Happy birthday to "+userName);
//     console.log("Happy birthday to you!");
//     console.log("You are",age," years old!");
// }


let width = window.prompt('Enter the width :');
let height = window.prompt('Enter the height :');
let area = getArea(width,height);

console.log('The area is',area);

function getArea(width,height){
    // let result = width*height;
    // return result
    return width * height
}