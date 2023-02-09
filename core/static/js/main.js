function filter_open() {
    var filter_block = document.getElementById('filter_block');
    filter_block.classList.toggle('active');
    var arrow_icon = document.getElementById('arrow_icon');
    arrow_icon.classList.toggle('active');
}

function modal_open() {
    var modal_block = document.getElementById('modal_block');
    modal_block.classList.toggle('active');
}