//array.map() = executes a provided callback function
//                         once for each array element
//                         AND creates a new array

// let numbers = [1, 2, 3, 4, 5];
// let squares = numbers.map(square);
// let cubes = numbers.map(square);
// cubes.forEach(print);

// function square(x){
//     return Math.pow(x,2);
// }
// function cube(x){
//     return Math.pow(x,3);
// }
// function print(x){
//     console.log(x);
// }


//array.filter() = creates a new array with all elements 
//                 that pass the test provided by a function

// let ages = [18, 15, 30, 40, 12, 90];
// let adults = ages.filter(checkAge);
// adults.forEach(print);

// function checkAge(age){
//     return age>=18;
// }
// function print(element){
//     console.log(element)
// }


//array.reduce() = reduces an array to a single value

// let prices = [5, 20, 49, 30, 26];
// let total = prices.reduce();

// console.log(`The total is $${total}`);

// function checkOut(total,element){
//     return total+element;
// }


let grades = [39, 30, 42, 85, 40, 93];

grades = grades.sort(ascendingSort);
grades.forEach(print)

function ascendingSort(x,y){
    return x - y;
}
function descendingSort(x,y){
    return y - x;
}
function print(element){
    console.log(element);
}