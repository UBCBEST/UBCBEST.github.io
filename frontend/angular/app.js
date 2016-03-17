(function () {
    angular.module('main', ['ngRoute'])
        .config(function ($routeProvider) {
            $routeProvider
                .when('/', {
                    templateUrl: 'angular/templates/welcome.html'
                })
                .when('/teams', {
                    templateUrl: 'angular/templates/teams.html'
                })
                .when('/projects', {
                    templateUrl: 'angular/templates/projects.html'
                })
                .otherwise({redirectTo: '/'});
        });
})();