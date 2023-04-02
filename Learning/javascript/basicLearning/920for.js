// for(let counter = 1;counter<=10;counter+=1){
//     console.log(counter);
// }

// for(let i = 1;i <= 10;i+=1){
//     console.log(i);
// }

// for(let j = 1; j <= 10;j+=1){
//     if(j == 6){
//         continue
//     }
//     else if(i==9){
//         break
//     }
//     console.log(j)
// }

// for(let i = 1;i <= 4;i+=1){
//     console.log('outter loop',i)
//     for(let j = 1; j <= 5;i+=1){
//         console.log('inner loop',j)
//     }
// }

let symbol = window.prompt("Enter a symbol to use: ");
let rows = window.prompt("Enter # of rows: ");
let cols = window.prompt("Enter # of columns: ");


for(let i = 1;i <= rows;i+=1){
    
    for(let j = 1; j <= cols;j+=1){
        document.getElementById('myRectangle').innerHTML += symbol;
    }
    document.getElementById('myRectangle').innerHTML += '<br>'
}