let menubar = document.querySelector('.menubar');
let menu = document.querySelector('.menu');
let closeMenu = document.querySelector('.close-menu');

menubar.addEventListener('click',()=>{
    menu.classList.add('active');
})

closeMenu.addEventListener('click',()=>{
    menu.classList.remove('active');
})