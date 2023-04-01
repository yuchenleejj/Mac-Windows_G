let a;
let b;
let c;

/*
a = window.prompt('Enter the side A:');
a = Number(a);

b = window.prompt('Enter the side B:');
b = Number(b);

c = math.pow(a,2) + math.pow(b,2);
c = math.sqrt(c);

console.log('The length of the hypotenuse is: ' + c);
*/

document.getElementById('submitButton').onclick = function(){
    a = document.getElementById('aTextBox').value;
    a = Number(a);

    b = document.getElementById('bTextBox').value;
    b = Number(b);

    c = Math.sqrt(Math.pow(a,2) + Math.pow(b,2));

    document.getElementById('cLabel').innerHTML = "Side C: " + c;
}

// Math 記得字首要大寫