$(document).ready(function(){

    $(".css .button").click(function(){
        event.preventDefault();
        var target = $(this)
        $(".css").removeClass("disabled");
        if ( target.closest(".css").hasClass("css-2009") ) {
            $('link[href="stylesheets/main_2012.css"]').attr('href','stylesheets/main_2009.css');
            $(".css-2012").addClass("disabled");
        } else {
            $('link[href="stylesheets/main_2009.css"]').attr('href','stylesheets/main_2012.css');
            $(".css-2009").addClass("disabled");
        }
    })

})