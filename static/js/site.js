$(document).ready(function(){

    var $nav = $('.navbar'),
        $body = $('body'),
        $window = $(window),
        navOffsetTop = $nav.offset().top,
        $document = $(document);

    function init(){
        $window.on('scroll', onScroll);
        $window.on('resize', resize);

    }

    function resize(){
        $body.removeClass('has-docked-nav');
        navOffsetTop = $nav.offset().top;
        onScroll();
    }
    
    function onScroll(){
        //console.log($window.scrollTop());
        if(navOffsetTop < $window.scrollTop() && !$body.hasClass('has-docked-nav')){
            $body.addClass('has-docked-nav');
        }
        if(navOffsetTop >= $window.scrollTop() && $body.hasClass('has-docked-nav')){
            $body.removeClass('has-docked-nav');
        }
    }

    init();
});

