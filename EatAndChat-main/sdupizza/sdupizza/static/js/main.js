window.addEventListener('DOMContentLoaded', function() {

    const slides = document.querySelectorAll('.offer__slide'),
          prev = document.querySelector('#offer__slider-prev'),
          next = document.querySelector('#offer__slider-next'),
          slideWrapper = document.querySelector('.offer__slider-wrapper'),
          slidesFiled = document.querySelector('.offer__slider-inner'),
          width = window.getComputedStyle(slidesFiled).width;
    
    let offset = 0;
    
    slidesFiled.style.width = width * slides.length + '%';
    slidesFiled.style.display = 'flex';
    slidesFiled.style.transition = '0.5s all';
    
    
    slides.forEach(slide => {
        slide.style.width = width + '%';
    })
    
    
    slideWrapper.style.overflow = 'hidden';

    
    next.addEventListener('click', () => {
    
        if (offset == +width.slice(0, width.length - 2) * (slides.length - 1)) {
            offset = 0;
        } else {
            offset += +width.slice(0, width.length - 2);
        }
    
        slidesFiled.style.transform = `translateX(-${offset}px)`;
    
    
    });
    
    
    prev.addEventListener('click', () => {
        if (offset == 0) {
            offset = +width.slice(0, width.length - 2) * (slides.length - 1);
        } else {
            offset -= +width.slice(0, width.length - 2);
        }
    
        slidesFiled.style.transform = `translateX(-${offset}px)`
    
    });
    
    });
    
    


 
    