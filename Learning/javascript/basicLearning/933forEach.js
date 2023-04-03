//array.forEach() = executes a provided callback function
//                  once for each array element

let students = ['spongebob','patrick','squidward'];
students.forEach(capitalize)
students.forEach(print)

// forEach mathod will automatically receive these three arguments
function capitalize(element, index, array){
    array[index] = element[0].toUpperCase() + element.substing(1);
}

function print(element){
    console.log(element)
}

console.log(students[0]);