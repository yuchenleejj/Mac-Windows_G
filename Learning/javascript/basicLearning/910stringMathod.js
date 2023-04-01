let username = 'justin';
let username1 = 'Miami';
let username2 = '  justin  ';
let username3 = '0903-999-403';

console.log(username.length);
console.log(username.charAt(2));
console.log(username.indexOf('u'));
console.log(username1.lastIndexOf('i'));
console.log(username2.trim());
console.log(username.toUpperCase());
console.log(username.toLowerCase());

username3 = username3.replace('-'," ");
console.log(username3);
