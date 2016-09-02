(function () {
    angular.module('app')
        .controller('teamsController', function (DataFactory, $scope) {
            $scope.selectedT = null;
            $scope.tabT = 0;

            function getTeam(tabT) {
                $scope.team = $scope.teams[tabT];
            }

            $scope.selectT = function (member) {
                $scope.selectedT = member;
            };

            $scope.isTabT = function (tab) {
                return tab === $scope.tabT;
            };

            $scope.setTabT = function (tab) {
                $scope.tabT = tab;
                getTeam(tab);
            };

            DataFactory.teams()
                .success(function (data) {
                    $scope.teams = data.data;
                    getTeam($scope.tabT);
                });
        })
        .directive('teamsDirective', function () {
            return {
                restrict: "E",
                templateUrl: "/static/angular/templates/teams.html",
                controller: "teamsController"
            }
        });
})();
