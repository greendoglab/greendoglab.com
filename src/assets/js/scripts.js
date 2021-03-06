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

    function Welcome() {

        $(window).on('scroll', function() {
            var scrollPos = $(this).scrollTop();
            var windowHeight = $(window).height();
            // siteName
            var siteName = $('.site-header');
            // fade & parallax
            var fadeStart=windowHeight/6;
            var fadeUntil=windowHeight/2;
            var elem = $('[data-type="parallax"]');

            // siteName action
            if (scrollPos >= (windowHeight-100)) {
                siteName.addClass('state');
            }
            else {
                siteName.removeClass('state');
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
        var elem = $('.discover');
        setTimeout(function() {
            elem.addClass('discover--active');
        }, 800);
    }

    function scrollToContent() {
        var trigger = $('[data-role="scroll-to-content"]');
        var windowHeight = $(window).height();
        trigger.click(function() {
            $('html, body').animate({
              scrollTop: windowHeight
            }, 1000);
        });
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
        Welcome();
        scrollDownShow();
        animateElements();
        scrollToContent();
    });

    // all initial on window resize
    // $(window).on('resize', function() {});


})(jQuery);
