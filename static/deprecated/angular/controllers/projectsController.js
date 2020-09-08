(function () {
    angular.module('app')
        .controller('projectsController', function (DataFactory, $scope) {
            $scope.selectedP = null;
            $scope.tabP = 0;

            function getProject(tabP) {
                $scope.project = $scope.projects[tabP];
            }

            $scope.selectP = function (member) {
                $scope.selectedP = member;
            };

            $scope.isTabP = function (tab) {
                return tab === $scope.tabP;
            };

            $scope.setTabP = function (tab) {
                $scope.tabP = tab;
                getProject(tab);
            };

            DataFactory.projects()
                .success(function (data) {
                    $scope.projects = data.data;
                    getProject($scope.tabP);
                });
        })
        .directive('projectsDirective', function () {
            return {
                restrict: "E",
                templateUrl: "/static/deprecated/angular/templates/projects.html",
                controller: "projectsController"
            }
        });
})();
