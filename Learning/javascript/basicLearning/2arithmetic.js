let student = 20;

student = student + 1;//- * / % 

console.log(student);

let extraStudent = student % 10;
let extraStudent1 = student ** 2;

console.log(extraStudent);
console.log(extraStudent1);

student+=1;
console.log(student);

// let student1+=1; this is wrong

// operator procedence
/* 
parenthesis>
exponentiation>
division/multiplication/modulus
>addition/subtraction
*/
let result = 2 + 3 * 4;
let result1 = (2 + 3) * 4;
console.log(result);
console.log(result1);