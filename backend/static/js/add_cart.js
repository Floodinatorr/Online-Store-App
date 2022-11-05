function addCart(id) {
    const count = document.getElementById('countInput');
    const countValue = count.value;
    const url = 'http://192.168.1.36/cart/add/' + id + '/' + countValue;
    console.log(url);
    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then((response) => response.json())
    .then((articles) => {
        if(articles.status == 'added_cart') {
            alert('Sepete eklendi');
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

