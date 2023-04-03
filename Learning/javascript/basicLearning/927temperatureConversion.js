document.getElementById('submitButton').onclick = function(){
    let temp;
    if(document.getElementById('cButton').checked){
        temp = document.getElementById('textBox').value;
        temp = Number(temp);
        temp = toCelsius(temp);
        document.getElementById('tempLabel').innerHTML = temp + '℃';
    }
    else if(document.getElementById('cButton').checked){
        temp = document.getElementById('textBox').value;
        temp = Number(temp);
        temp = toFahrenheit(temp);
        document.getElementById('tempLabel').innerHTML = temp + '℉';
    }
    else{
        document.getElementById("tempLabel").innerHTML = 'Select a Unit';
    }
}


function toFahrenheit(temp){
    return (temp - 32) * (5/9);
}
function toCelsius(temp){
    return temp * 9/5 + 32;
}