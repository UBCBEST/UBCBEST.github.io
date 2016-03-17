angular.module('main')
    .directive('best', function () {
        return {
            restrict: 'E',
            templateUrl: 'angular/templates/header.html'
        };
    })
    .directive('connect', function () {
        return {
            restrict: 'E',
            templateUrl: 'angular/templates/footer.html'
        };
    });

