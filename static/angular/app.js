(function () {
    angular.module('main', ['ngRoute'])
        .config(function ($routeProvider) {
            $routeProvider
                .when('/', {
                    templateUrl: '/templates/welcome.html'
                })
                .when('/teams', {
                    templateUrl: '/templates/teams.html'
                })
                .when('/projects', {
                    templateUrl: '/templates/projects.html'
                })
                .otherwise({redirectTo: '/'});
        })
        .config(['$interpolateProvider', function ($interpolateProvider) {
            $interpolateProvider.startSymbol('{[');
            $interpolateProvider.endSymbol(']}');
        }]);
})();
