angular.module('main')
    .directive('best', function () {
        return {
            restrict: 'E',
            templateUrl: '/static/angular/templates/header.html'
        };
    })
    .directive('connect', function () {
        return {
            restrict: 'E',
            templateUrl: '/static/angular/templates/footer.html'
        };
    });
