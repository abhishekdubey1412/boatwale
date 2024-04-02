// Navbar Section
let menu_btn = document.getElementsByClassName('bi-three-dots')[0];
let menu_bx = document.getElementById('menu_bx');

menu_btn.addEventListener('click', ()=>{
    menu_bx.classList.toggle('ul_active');
});