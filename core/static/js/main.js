function filter_open() {
    var filter_block = document.getElementById('filter_block');
    filter_block.classList.toggle('active');
    var arrow_icon = document.getElementById('arrow_icon');
    arrow_icon.classList.toggle('active');
}

function modal_open(name) {
    console.log(name)
    var modal_block = document.getElementsByName(name)[0];
    modal_block.classList.toggle('active');
}
