(function () {
    angular.module('app')
        .directive('projectsDirective', function () {
            return {
                restrict: "E",
                templateUrl: "/static/angular/templates/projects.html",
                controller: "projectsController",
                link: function (scope, element) {
                    var children = $(element).find('.profile-wrapper');
                    for (var ii = 0; ii < children.length; ++ii) {
                        $(children[ii]).stellar({
                            horizontalScrolling: true,
                            verticalScrolling: false
                        })
                    }
                }
            }
        });
})();
