$(document).ready(function () {
    $('.owl-carousel').owlCarousel({

        loop:true,
        margin:10,
        center:true,
        autoplay:true,
        nav:false,
        dots:false,
        autoWidth:true,
        responsive:{
            200:{
                items:1
            },
            600:{
                items:3
            },
            1000:{
                items:3
            }
        }
    })
    
})

