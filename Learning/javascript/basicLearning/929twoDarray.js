let fruits = ['apples','oranges','bananas'];
let vegetables = ['carrots','onions','potatoes'];
let meats = ['eggs','chickens','fish'];

let groceryList = [fruits, vegetables, meats];

groceryList[0][2] = 'mangoes';

for(let list of groceryList){
    for(let food of list){
        console.log(food);
    }
}