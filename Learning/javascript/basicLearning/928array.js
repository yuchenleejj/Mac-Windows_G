let fruits = ["apple", "orange", "banana"];

//fruits[2] = "coconut";

//fruits.push("lemon");      //add an element
//fruits.pop();                     //removes last element
//fruits.unshift("mango"); //add element to beginning
//fruits.shift();                   //removes element from beginning

//let length = fruits.length;
//let index = fruits.indexOf("kiwi");

// for(let i = 0;i < fruits.length;i+=1){
//     console.log(fruits[i]);
// }

// for(let i = fruits.length - 1;i >= 0;i-=1){
//     console.log(fruits[i]);
// }

// for(let fruit of fruits){
//     console.log(fruit);
// }


fruits = fruits.sort().reverse();

for(let fruit of fruits){
    console.log(fruit);
}



console.log(fruits);