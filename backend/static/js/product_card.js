function showCard(id) {
    const like = document.getElementById('likeButton-' + id);
    const cart = document.getElementById('cartButton-' + id);
    
    like.classList.remove('hideInfo');
    like.classList.toggle('showInfo');
    cart.classList.remove('hideInfo');
    cart.classList.toggle('showInfo');
}

function hideCard(id) {
    const like = document.getElementById('likeButton-' + id);
    const cart = document.getElementById('cartButton-' + id);
    
    like.classList.toggle('hideInfo');
    like.classList.remove('showInfo');
    cart.classList.toggle('hideInfo');
    cart.classList.remove('showInfo');
}