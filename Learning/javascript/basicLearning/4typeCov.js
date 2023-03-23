let age = window.prompt('What is your age?');
console.log(typeof age);
age = Number(age);
console.log(typeof age);
age += 1;
console.log("Happy Birthday! You are "+age+" years old now.");

let x;
let x1;
let y;
let z;
let z1;
let z2;

x = Number('3.14');
x1 = Number('3.14abc');
y = String(3.14);
z = Boolean(''); // empty string is false otherwise true
z1 = Boolean(1);
z2 = Boolean(0);

console.log(x,typeof x);
console.log(x1,typeof x1);
console.log(y,typeof y);
console.log(z,typeof z);
console.log(z1,typeof z1);
console.log(z2,typeof z2);