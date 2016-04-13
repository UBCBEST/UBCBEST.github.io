(function () {
    angular.module('main')
        .directive('projectsDirective', function () {
            return {
                restrict: "E",
                templateUrl: "/static/angular/templates/projects.html",
                controller: "projectsController"
            }
        });
})();
