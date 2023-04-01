let fullName = 'Justin Lee';
let lastName;
let firstName;

// firstName = fullName.slice(0,6);
// lastName = fullName.slice(7);
firstName = fullName.slice(0,fullName.indexOf(" "));
lastName = fullName.slice(fullName.indexOf(" ")+1);

console.log('first name is '+firstName)
console.log('last name is '+lastName)