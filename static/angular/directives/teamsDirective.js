(function () {
    angular.module('main')
        .directive('teamsDirective', function () {
            return {
                restrict: "E",
                templateUrl: "/static/angular/templates/teams.html",
                controller: "teamsController"
            }
        });
})();
