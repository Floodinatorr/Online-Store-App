const increase = document.getElementById('countIncrease');
const decrease = document.getElementById('countDecrease');
const input = document.getElementById('countInput');

increase.addEventListener('click', () => {
    input.value = parseInt(input.value) + 1;
});

decrease.addEventListener('click', () => {
    if(input.value > 1){
        input.value = parseInt(input.value) - 1;
    }
});