let adult = checkAge(21);
console.log(adult);

function checkAge(age){
    // if(age >= 18){
    //     return true;
    // }
    // else{
    //     return false;
    // }
    return age >= 18 ? true:false
}

checkWinner(true);

function checkWinner(win){
    win ? console.log('YOU WIN!'):console.log('YOU LOSE!')
}