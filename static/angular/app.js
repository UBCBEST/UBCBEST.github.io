(function () {
    angular.module('main', ['ngRoute', 'angular-parallax'])
        .config(function ($routeProvider) {
            $routeProvider
                .when('/', {
                    templateUrl: 'static/angular/templates/welcome.html'
                })
                .when('/teams', {
                    templateUrl: 'static/angular/templates/teams.html'
                })
                .when('/projects', {
                    templateUrl: 'static/angular/templates/projects.html'
                })
                .otherwise({redirectTo: '/'});
        })
        .config(['$interpolateProvider', function ($interpolateProvider) {
            $interpolateProvider.startSymbol('{[');
            $interpolateProvider.endSymbol(']}');
        }]);
})();
