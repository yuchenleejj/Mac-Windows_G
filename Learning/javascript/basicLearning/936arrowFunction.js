// arrow function expression = compact alternative to a traditional function expression
//      =>

// const greeting = function(userName){
//     console.log(`Hello ${userName}`);
// }

const greeting = (userName) => console.log(`Hello ${userName}`);
// no argument() ,one argument(x) or x ,more argument(x,y,z)
greeting('Bro');

// example1
let grades = [100, 40, 49, 50, 40, 20];

grades.sort((x,y) => y - x);
grades.forEach((element) => console.log(element))

// the script behind the => means return