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

/*Form Status Checker*/

function formSubmit(event) {
    var modal_order__status = document.getElementById('modal_order__status');
    modal_order__status.classList.add('active');
    event.preventDefault();
}

const modal_form = document.getElementById('modal_form');

if (modal_form) {
    modal_form.addEventListener('submit', formSubmit);   
}

/*------------------------*/


function product_open() {
    var product_open = document.getElementsByName();
    product_open.classList.toggle('active');
}

/*Animation Burger Menu*/

var body = document.getElementsByTagName('body')[0];

        // trigger this function every time the user scrolls
        window.onscroll = function (event) {
            var scroll = window.pageYOffset;
            var burger = document.getElementById('burger_block');
            if (scroll > 10) {
                burger.classList.add('active');
            } 

            else {
                burger.classList.remove('active');
            }
        }
/*----------------------- */

/*Video Open Function */
function video_open(number){
    var video_modal = document.getElementById('video_modal');
    var video_first = document.getElementById('video_first');
    var video_second = document.getElementById('video_second');
    var video_third = document.getElementById('video_third');

    if (number == 1) {
        video_first.classList.add('active');
        video_modal.classList.add('active');
    }else if(number == 2){
        video_second.classList.add('active');
        video_modal.classList.add('active');
    } else if(number == 3){
        video_third.classList.add('active');
        video_modal.classList.add('active');
    } else if(number == 99){
        video_modal.classList.remove('active');
        video_first.classList.remove('active');
        video_second.classList.remove('active');
        video_third.classList.remove('active');
    }
    
}
/*-------------------- */

function product_checker(number){
    if (number) {
            var opt= document.getElementById('checker');
            opt.value =  number;
            opt.text = number;
            console.log(number);
    }
}

