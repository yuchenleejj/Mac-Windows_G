let grade = "A";

switch(grade){
    case "A":
        console.log('You are great!');
        break;
    case "B":
        console.log('You are good!');
        break;
    case "C":
        console.log('You are okay!');
        break;
    case "D":
        console.log('You passed ... barely!');
        break;
    case "F":
        console.log('You FAILED!');
        break;
    default:
        console.log(grade,'is not a letter grade!')
}

let grade1 = 70;
switch(true){
    case grade1 >= 90:
        console.log('You are great!');
        break;
    case grade1 >= 80:
        console.log('You are good!');
        break;
    case grade1 >= 70:
        console.log('You are okay!');
        break;
    case grade1 >= 60:
        console.log('You passed ... barely!');
        break;
    case grade1 < 60:
        console.log('You FAILED!');
        break;
    default:
        console.log(grade,'is not a letter grade!')
}