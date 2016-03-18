(function () {
    angular.module('main')
        .controller('welcomeController', function() {
            $('.parallax-window').parallax({imgSrc: '../../../static/img/landing-parallax.jpg'});
        });
})();
