(function () {
    angular.module('app')
        .directive('projectsDirective', function () {
            return {
                restrict: "E",
                templateUrl: "/static/angular/templates/projects.html",
                controller: "projectsController"
            }
        });
})();
