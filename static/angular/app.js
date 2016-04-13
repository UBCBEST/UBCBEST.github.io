(function () {
    angular.module('main', ['angular-parallax'])
        .config(['$interpolateProvider', function ($interpolateProvider) {
            $interpolateProvider.startSymbol('{[');
            $interpolateProvider.endSymbol(']}');
        }])
        .run(function ($rootScope) {
            new WOW().init();
        });
})();
