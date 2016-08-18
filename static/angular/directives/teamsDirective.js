(function () {
    angular.module('app')
        .directive('teamsDirective', function () {
            return {
                restrict: "E",
                templateUrl: "/static/angular/templates/teams.html",
                controller: "teamsController",
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
