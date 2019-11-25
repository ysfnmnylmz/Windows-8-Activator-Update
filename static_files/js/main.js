$('.owl-carousel').owlCarousel({
    loop: false,
    items: 8,
    center:false,
    responsive: {
        0: {
            items: 2,
            center:true,
        },
        480: {
            items: 3,
            center:true
        },
        600: {
            items: 4,
            center:true
        },
        768: {
            items: 5
        },
        1000: {
            items: 7
        },
        1200:{
            items:8
        },
        1336:{
            items:10
        }
    }
})