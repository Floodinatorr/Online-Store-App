const gridButton = document.querySelectorAll('.gridButton');
const needRow = document.getElementById('needRow');

gridButton.forEach((button) => {
    button.addEventListener('click', () => {
        gridButton.forEach((button) => {
            button.classList.remove('buttonActive');
        });
        button.classList.add('buttonActive');
        if (button.classList.contains('twoGrid')) {
            needRow.classList.remove('row-cols-md-3');
            needRow.classList.remove('row-cols-md-4');
            needRow.classList.add('row-cols-md-2');
        } else if (button.classList.contains('threeGrid')) {
            needRow.classList.remove('row-cols-md-2');
            needRow.classList.remove('row-cols-md-4');
            needRow.classList.add('row-cols-md-3');
        } else if (button.classList.contains('fourGrid')) {
            needRow.classList.remove('row-cols-md-2');
            needRow.classList.remove('row-cols-md-3');
            needRow.classList.add('row-cols-md-4');
        } else {
            alert('Error in Grid Buttons!');
        }
    });
});