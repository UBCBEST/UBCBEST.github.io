(function () {
    angular.module('app', ['angular-parallax', 'ng-counter'])
        .config(['$interpolateProvider', function ($interpolateProvider) {
            $interpolateProvider.startSymbol('{[');
            $interpolateProvider.endSymbol(']}');
        }])
        .run(function ($rootScope) {
            new WOW().init();
        });
})();
