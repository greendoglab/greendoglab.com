(function($) {

    function stateCheck(elem, clName) {
        $el = elem;
        $clName = clName
        if (!$el.hasClass(clName)) {
            $el.addClass(clName);
        } else {
            $el.removeClass(clName);
        }
    }

    function mainMenu() {
        var trigger = $('[data-role="menu-trigger"]');
        var menu = $('[data-role="menu"]');
        var body = $('body');

        trigger.click(function() {
            $(this).toggleClass('active');
            stateCheck(menu, 'active');
            stateCheck(body, 'open-menu');
        });
    }

    // document ready
    $(window).on('load', function() {
        mainMenu()
    });

    // all initial on window resize
    $(window).on('resize', function() {});


})(jQuery);
