(function () {
    angular.module('app')
        .controller('teamsController', function (DataFactory, $scope) {
            $scope.selectedT = null;
            $scope.tabT = 0;

            function getTeam(tabT) {
                DataFactory.getTeam(tabT)
                    .success(function (data) {
                        $scope.team = data;
                    });
            }

            DataFactory.teams()
                .success(function (data) {
                    $scope.teams = data.data;
                });

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

            getTeam($scope.tabT);
        });
})();
