// #DEV: code for image gallery 
let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("demo");
    let captionText = document.getElementById("caption");

    if (n > slides.length) { slideIndex = 1; }
    if (n < 1) { slideIndex = slides.length; }

    for (let i = 0; i < slides.length; i++) {
        slides[i].classList.add("hidden");
    }
    for (let i = 0; i < dots.length; i++) {
        dots[i].classList.remove("opacity-100");
        dots[i].classList.add("opacity-60");
    }

    slides[slideIndex - 1].classList.remove("hidden");
    dots[slideIndex - 1].classList.remove("opacity-60");
    dots[slideIndex - 1].classList.add("opacity-100");
    captionText.innerHTML = dots[slideIndex - 1].alt;
}
// ------------------------------------------------------------------------------------------------------


// #DEV: code for navbar 
// Load navbar dynamically
document.addEventListener('DOMContentLoaded', function () {
    const menuBtn = document.getElementById('menuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    const mobileLinks = mobileMenu.querySelectorAll('a');

    // Toggle menu visibility
    menuBtn.addEventListener('click', function () {
        mobileMenu.classList.toggle('hidden');
    });

    // Close mobile menu on link click
    mobileLinks.forEach(link => {
        link.addEventListener('click', function () {
            mobileMenu.classList.add('hidden');
        });
    });
});


// #DEV: code for slide careousel
$(document).ready(function () {
    $('.owl-carousel').owlCarousel({
        loop: true,
        nav: true,
        dots: true,
        autoplay: true,
        mouseDrag: false,
        animateOut: 'slideOutUp',
        responsive: {
            0: {
                items: 1,
            },
            600: {
                items: 1,
            },
            1000: {
                items: 1,
            }
        }
    });
});