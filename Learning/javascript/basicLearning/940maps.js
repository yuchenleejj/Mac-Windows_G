// Map = object that holds key-value pairs of any data type
// like dictionary in python

const store = new Map([
    ["t-shirt", 20],
    ["jeans", 30],
    ["socks", 10],
    ["underwear", 50]
]);

let shoppingCart = 0;
shoppingCart+=store.get("t-shirt");
console.log(shoppingCart);
store.set("hat",40);
store.delete('hat');
console.log(store.has('hat'))
console.log(store.size)

store.forEach((value,key)=> console.log(`${key} $${value}`))