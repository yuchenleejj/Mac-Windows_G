let userName = 'Justin';
let items = 3;
let total = 75;

console.log(`Hello ${userName}`);
console.log(`You have ${items} items in your cart`);
console.log(`Your total is ${total}`);

// remember to use the ` backtick instead of ' or "
// let text = 
// `Hello ${userName}
// You have ${items} items in your cart
// Your total is ${total}`;

// console.log(text);
let text = 
`Hello ${userName}<br>
You have ${items} items in your cart<br>
Your total is ${total}<br>`;

document.getElementById('myLabel').innerHTML = text ;

