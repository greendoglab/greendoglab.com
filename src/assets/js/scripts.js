(function($) {

    // reusable functions
    function stateCheck(elem, clName) {
        $el = elem;
        $clName = clName
        if (!$el.hasClass(clName)) {
            $el.addClass(clName);
        } else {
            $el.removeClass(clName);
        }
    }

    function equalheight(container) {

        var currentTallest = 0,
        currentRowStart = 0,
        rowDivs = new Array(),
        $el,
        topPosition = 0;

        $(container).each(function() {

            $el = $(this);
            $($el).height('auto')
            topPostion = $el.position().top;

            if (currentRowStart != topPostion) {
                for (currentDiv = 0 ; currentDiv < rowDivs.length ; currentDiv++) {
                    rowDivs[currentDiv].height(currentTallest);
                }
                rowDivs.length = 0; // empty the array
                currentRowStart = topPostion;
                currentTallest = $el.height();
                rowDivs.push($el);
            } else {
                rowDivs.push($el);
                currentTallest = (currentTallest < $el.height()) ? ($el.height()) : (currentTallest);
            }
            for (currentDiv = 0 ; currentDiv < rowDivs.length ; currentDiv++) {
                    rowDivs[currentDiv].height(currentTallest);
            }
        });
    }

    // site functions
    function RandomBack() {
        var images = [
            'back2.jpg',
            'back4.jpg',
            'back6.jpg',
            'back7.jpg',
        ];

        $('.welcome').css({'background-image': 'url(/static/images/' + images[Math.floor(Math.random() * images.length)] + ')'});
    }

    function Welcome() {

        $(window).on('scroll', function() {
            var scrollPos = $(this).scrollTop();
            var windowHeight = $(window).height();
            // siteName
            var siteName = $('.green-word');
            // fade & parallax
            var fadeStart=windowHeight/6;
            var fadeUntil=windowHeight/2;
            var elem = $('[data-type="parallax"]');

            // siteName action
            if (scrollPos >= (windowHeight-100)) {
                console.log('sucsess');
                siteName.addClass('shadows');
            }
            else {
                siteName.removeClass('shadows');
            }

            // parallax action
            elem.each(function(){
                var block = $(this);
                var opacity = 0;

                var offset = $(window).scrollTop();
                var diff = offset / block.data('speed');
                block.css({ marginTop: -diff });
                console.log(diff);
                if( offset<=fadeStart ){
                    opacity=1;
                }else if( offset<=fadeUntil ){
                    opacity=1-offset/fadeUntil;
                }
                block.css('opacity',opacity);

            });
        });
    }

    function scrollDownShow() {
        var elem = $('.scroll-down');
        setTimeout(function() {
            elem.addClass('active');
        }, 800);
    }

    function animateElements() {
        var ANIMATION_CLASS = 'state';
        $(window).on('scroll', function() {
            var scrollPos = $(this).scrollTop() + $(this).height() - 20;

            $('[data-role="animate-scroll"]').each(function() {
                var el = $(this);
                // console.log(el, el.offset().top, scrollPos);
                if (scrollPos >= el.offset().top && !el.hasClass(ANIMATION_CLASS)) {
                    el.addClass(ANIMATION_CLASS);
                }
                if (scrollPos < el.offset().top && el.hasClass(ANIMATION_CLASS)) {
                    el.removeClass(ANIMATION_CLASS);
                }
            });
        });
    }

    // document ready
    $(window).on('load', function() {
        equalheight('.works .work .work-info');
        RandomBack();
        Welcome();
        scrollDownShow();
        animateElements();
    });

    // all initial on window resize
    // $(window).on('resize', function() {});


})(jQuery);
