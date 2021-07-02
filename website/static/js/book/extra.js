$(document).ready(function (){
    let scolling = false
    $("#find-current").click(function (){
        if (!scolling) {
            scolling = true
            $('html').animate({
                scrollTop: $("#active").offset().top
            }, 2000);
            setTimeout(() => scolling = false, 2000)
        }
    });
});