(function () {
    angular.module('app')
        .controller('teamsController', function (DataFactory, $scope) {
            $scope.selectedT = null;
            $scope.tabT = 0;

            $scope.selectT = function (member) {
                $scope.selectedT = member;
            };

            DataFactory.teams()
                .success(function (data) {
                    $scope.teams = data.data;
                });

            $scope.isTabT = function (tab) {
                return tab === $scope.tabT;
            }
        });
})();
